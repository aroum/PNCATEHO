import numpy as np
import sounddevice as sd
import scipy.signal

class Voice:
    def __init__(self, engine):
        self.engine = engine
        self.active = False
        self.note_freq = 440.0
        self.gate = False
        
        # Internal Voice State
        self.phase = {"VCO1": 0.0, "VCO2": 0.0}
        self.env_state = {"EG1": 0, "EG2": 0} 
        self.env_val = {"EG1": 0.0, "EG2": 0.0}
        self.filter_state = {
            "VCF1": np.zeros(2), "VCF2": np.zeros(2)
        }

    def note_on(self, freq):
        self.note_freq = freq
        self.gate = True
        self.active = True
        for eg in ["EG1", "EG2"]:
            self.env_state[eg] = 1 # Attack

    def note_off(self):
        self.gate = False
        for eg in ["EG1", "EG2"]:
            self.env_state[eg] = 3 # Release

    def _get_envelope(self, name, frames):
        p = self.engine.params[name]
        attack_s = p["attack"] * 2.0 + 0.01
        decay_s = p["decay"] * 2.0 + 0.01
        release_s = p["release"] * 2.0 + 0.01
        
        attack_rate = 1.0 / (attack_s * self.engine.sample_rate)
        decay_rate = 1.0 / (decay_s * self.engine.sample_rate)
        release_rate = 1.0 / (release_s * self.engine.sample_rate)
        
        current = self.env_val[name]
        state = self.env_state[name]
        
        target = 0.0
        rate = 0.0
        
        if state == 1: # Attack
            target = 1.0
            rate = attack_rate
        elif state == 2: # Decay (to sustain)
            target = 0.5 # Fixed sustain
            rate = decay_rate
        elif state == 3: # Release
            target = 0.0
            rate = release_rate
        else: # Idle
            target = 0.0
            rate = 1.0 
        
        step = rate * frames
        if current < target:
            next_val = min(current + step, target)
            if next_val >= target and state == 1:
                self.env_state[name] = 2 
        elif current > target:
            next_val = max(current - step, target)
        else:
            next_val = target
            
        vals = np.linspace(current, next_val, frames)
        self.env_val[name] = next_val
        
        if state == 1 and next_val >= 1.0:
            self.env_state[name] = 2
        
        if state == 3 and next_val <= 0.001:
            self.env_state[name] = 0 # Idle
            self.env_val[name] = 0.0
            
        return vals

    def _oscillator(self, name, freq, frames, lfo_mod=0):
        p = self.engine.params[name]
        detune = (p["pitch"] - 0.5) * 2.0
        base_freq = freq * (2.0 ** detune)
        
        f = base_freq * (1.0 + lfo_mod * 0.1) 
        phase_inc = f * (1.0/self.engine.sample_rate)
        
        if np.isscalar(phase_inc):
            phase_deltas = np.full(frames, phase_inc)
        else:
            phase_deltas = phase_inc
            
        phases = self.phase[name] + np.cumsum(phase_deltas)
        self.phase[name] = phases[-1] % 1.0
        phases = phases % 1.0
        
        wave_param = p["wave"]
        
        saw = 2.0 * phases - 1.0
        square = np.sign(phases - 0.5)
        sine = np.sin(2.0 * np.pi * phases)
        
        if wave_param < 0.5:
            mix = wave_param * 2.0 
            out = (1.0 - mix) * saw + mix * square
        else:
            mix = (wave_param - 0.5) * 2.0
            out = (1.0 - mix) * square + mix * sine
            
        return out * p["level"]

    def _filter(self, name, signal, env_val):
        p = self.engine.params[name]
        cutoff_norm = p["cutoff"]
        env_mod = np.mean(env_val) if not np.isscalar(env_val) else env_val
        
        cutoff_mod = cutoff_norm + (env_mod * p["env_amt"])
        cutoff_mod = np.clip(cutoff_mod, 0.0, 1.0)
        
        freq = 20.0 * (500.0 ** cutoff_mod)
        if freq > 10000.0: freq = 10000.0
        
        res = p["res"] * 0.95
        
        # Use Engine's biquad helper or just copy logic? 
        # Easier to call engine._biquad logic here directly or via helper.
        # But _biquad in Engine is designed for general use.
        # Let's use scipy.signal.lfilter directly here as in original code for efficiency
        
        w0 = 2 * np.pi * freq / self.engine.sample_rate
        cos_w0 = np.cos(w0)
        alpha = np.sin(w0) * (1 - res)
        
        b0 = (1 - cos_w0) / 2
        b1 = 1 - cos_w0
        b2 = (1 - cos_w0) / 2
        a0 = 1 + alpha
        a1 = -2 * cos_w0
        a2 = 1 - alpha
        
        b = np.array([b0, b1, b2]) / a0
        a = np.array([a0, a1, a2]) / a0
        
        out, self.filter_state[name] = scipy.signal.lfilter(b, a, signal, zi=self.filter_state[name])
        return out

    def process(self, frames, lfo1, lfo2, noise_ch1, noise_ch2):
        if not self.active:
            return np.zeros(frames)
            
        eg1 = self._get_envelope("EG1", frames)
        eg2 = self._get_envelope("EG2", frames)
        
        # Auto-deactivate if silent
        if (self.env_state["EG1"] == 0 and self.env_val["EG1"] < 0.001 and 
            self.env_state["EG2"] == 0 and self.env_val["EG2"] < 0.001):
            self.active = False
            return np.zeros(frames)
            
        vco1 = self._oscillator("VCO1", self.note_freq, frames, lfo_mod=lfo1)
        vco2 = self._oscillator("VCO2", self.note_freq, frames, lfo_mod=lfo2)
        
        vcf1_in = vco1 + noise_ch1
        vcf1_out = self._filter("VCF1", vcf1_in, eg1)
        vcf1_out *= eg1
        
        vcf2_in = vco2 + noise_ch2
        vcf2_out = self._filter("VCF2", vcf2_in, eg2)
        vcf2_out *= eg2
        
        return vcf1_out + vcf2_out


class AudioEngine:
    def __init__(self, sample_rate=44100, block_size=512):
        self.sample_rate = sample_rate
        self.block_size = block_size
        self.active = False
        self.stream = None

        # Global State
        self.params = {
            "VCO1": {"pitch": 0.5, "wave": 0.0, "level": 0.5},
            "VCF1": {"cutoff": 1.0, "res": 0.0, "env_amt": 0.0},
            "LFO1": {"rate": 0.2, "wave": 2.0, "amt": 0.0},
            "EG1":  {"attack": 0.1, "decay": 0.3, "release": 0.5},
            
            "VCO2": {"pitch": 0.5, "wave": 0.0, "level": 0.0},
            "VCF2": {"cutoff": 1.0, "res": 0.0, "env_amt": 0.0},
            "LFO2": {"rate": 0.2, "wave": 2.0, "amt": 0.0},
            "EG2":  {"attack": 0.1, "decay": 0.3, "release": 0.5},
            
            "NOISE": {"pitch": 0.5, "filt": 0.0, "level": 0.0},
            "FX":    {"delay_time": 0.0, "feedback": 0.0, "mix": 0.0},
        }

        # Global LFO/Noise state
        self.phase = {"LFO1": 0.0, "LFO2": 0.0}
        self.filter_state = {"noise_color": np.zeros(2)}
        
        # Polyphony
        self.MAX_VOICES = 8
        self.voices = [Voice(self) for _ in range(self.MAX_VOICES)]
        
        self.scope_buffer = np.zeros(block_size) 
        self.delay_buffer = np.zeros(self.sample_rate * 2)
        self.delay_ptr = 0

    def start(self):
        if self.active: return
        self.stream = sd.OutputStream(
            channels=1, 
            samplerate=self.sample_rate, 
            blocksize=self.block_size,
            callback=self.audio_callback
        )
        self.stream.start()
        self.active = True

    def stop(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
        self.active = False

    def note_on(self, freq):
        # 1. Check if note already playing (Retrigger)
        for v in self.voices:
            if v.active and abs(v.note_freq - freq) < 0.1:
                v.note_on(freq)
                return
        
        # 2. Find free voice
        for v in self.voices:
            if not v.active:
                v.note_on(freq)
                return
                
        # 3. Steal voice (oldest/released? Simplest: first one)
        # Ideally we steal one in release phase.
        for v in self.voices:
            if v.env_state["EG1"] == 3: # Release
                v.note_on(freq)
                return
                
        # 4. Hard steal
        self.voices[0].note_on(freq)
        # Rotate list to make this one last next time?
        self.voices.append(self.voices.pop(0))

    def note_off(self, freq):
        # Find voice playing this note
        for v in self.voices:
            if v.active and abs(v.note_freq - freq) < 0.1:
                v.note_off()
                # Don't break, in case multiple voices have same note (unlikely but safe)

    def _lfo(self, name, frames):
        p = self.params[name]
        rate = p["rate"] * 20.0
        phase_inc = rate / self.sample_rate
        phases = self.phase[name] + np.cumsum(np.full(frames, phase_inc))
        self.phase[name] = phases[-1] % 1.0
        phases = phases % 1.0
        
        wave_param = p["wave"]
        
        saw = 2.0 * phases - 1.0
        square = np.sign(phases - 0.5)
        sine = np.sin(2.0 * np.pi * phases)
        
        if wave_param < 0.5:
            mix = wave_param * 2.0 
            out = (1.0 - mix) * saw + mix * square
        else:
            mix = (wave_param - 0.5) * 2.0
            out = (1.0 - mix) * square + mix * sine
        
        return out * p["amt"]

    def _biquad(self, signal, freq, q, f_type, state_name):
        w0 = 2 * np.pi * freq / self.sample_rate
        cos_w0 = np.cos(w0)
        sin_w0 = np.sin(w0)
        alpha = sin_w0 / (2 * q)
        
        if f_type == "lp":
            b0 = (1 - cos_w0) / 2
            b1 = 1 - cos_w0
            b2 = (1 - cos_w0) / 2
            a0 = 1 + alpha
            a1 = -2 * cos_w0
            a2 = 1 - alpha
        elif f_type == "hp":
            b0 = (1 + cos_w0) / 2
            b1 = -(1 + cos_w0)
            b2 = (1 + cos_w0) / 2
            a0 = 1 + alpha
            a1 = -2 * cos_w0
            a2 = 1 - alpha
        else:
            return signal
            
        b = np.array([b0, b1, b2]) / a0
        a = np.array([a0, a1, a2]) / a0
        
        zi = self.filter_state.get(state_name, np.zeros(2))
        out, zi = scipy.signal.lfilter(b, a, signal, zi=zi)
        self.filter_state[state_name] = zi
        return out

    def _noise_gen(self, frames):
        p = self.params["NOISE"]
        noise = (np.random.random(frames) * 2.0 - 1.0)
        f_val = p["filt"]
        
        if f_val > 0.55: 
            norm = (f_val - 0.55) / 0.45
            fc = 20000.0 * (0.005 ** norm)
            noise = self._biquad(noise, fc, 0.707, "lp", "noise_color")
        elif f_val < 0.45: 
            norm = (0.45 - f_val) / 0.45
            fc = 20.0 * (500.0 ** norm)
            noise = self._biquad(noise, fc, 0.707, "hp", "noise_color")
            
        return noise

    def audio_callback(self, outdata, frames, time, status):
        if status:
            print(status)
        
        outdata.fill(0)
        
        # Global Modulators
        lfo1 = self._lfo("LFO1", frames)
        lfo2 = self._lfo("LFO2", frames)
        
        # Global Noise
        noise_raw = self._noise_gen(frames)
        p_noise = self.params["NOISE"]
        noise_ch1 = noise_raw * p_noise["pitch"]
        noise_ch2 = noise_raw * p_noise["level"]
        
        # Sum Voices
        mix = np.zeros(frames)
        active_count = 0
        
        for voice in self.voices:
            if voice.active:
                mix += voice.process(frames, lfo1, lfo2, noise_ch1, noise_ch2)
                active_count += 1
                
        # Normalize? With polyphony, levels can get high.
        # Soft clip
        mix = np.tanh(mix * 0.5) 
        
        # FX (Delay)
        fx_p = self.params["FX"]
        delay_mix = fx_p["mix"]
        if delay_mix > 0.01:
            d_time_s = fx_p["delay_time"] * 1.0 
            d_samples = int(d_time_s * self.sample_rate)
            d_samples = max(1, min(d_samples, len(self.delay_buffer) - frames))
            
            read_ptr = (self.delay_ptr - d_samples) % len(self.delay_buffer)
            indices = (np.arange(frames) + read_ptr) % len(self.delay_buffer)
            delayed_sig = self.delay_buffer[indices]
            
            feedback_sig = mix + delayed_sig * fx_p["feedback"]
            
            # Write to buffer
            w_indices = (np.arange(frames) + self.delay_ptr) % len(self.delay_buffer)
            self.delay_buffer[w_indices] = feedback_sig
            self.delay_ptr = (self.delay_ptr + frames) % len(self.delay_buffer)
            
            mix = mix * (1.0 - delay_mix) + delayed_sig * delay_mix
            
        self.scope_buffer = mix # Update scope
        
        outdata[:] = mix.reshape(-1, 1)
