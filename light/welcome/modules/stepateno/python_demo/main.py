import sys
import numpy as np
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QGridLayout, QPushButton, QLabel, QDial, QFrame, QSizePolicy)
from PySide6.QtCore import Qt, Slot, QTimer, QPointF
from PySide6.QtGui import QPainter, QColor, QPen
from audio_engine import AudioEngine

class OscilloscopeWidget(QWidget):
    def __init__(self, engine, parent=None):
        super().__init__(parent)
        self.engine = engine
        self.setMinimumHeight(200) # Double height
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setAttribute(Qt.WA_StyledBackground, True)
        
        # Timer for 60 FPS update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_scope)
        self.timer.start(16)
        
    def update_scope(self):
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        width = self.width()
        height = self.height()
        half_width = width // 2
        
        # Draw Scope (Left Half)
        data = self.engine.scope_buffer
        if data is None or len(data) == 0:
            return
            
        # Synchronization (Zero Crossing Trigger)
        # Find first point where value crosses 0 from negative to positive
        trigger_idx = 0
        for i in range(len(data) - 1):
            if data[i] <= 0 and data[i+1] > 0:
                trigger_idx = i
                break
        
        # If we found a trigger, start from there. 
        # But ensure we have enough data left.
        # If not triggered or near end, just show from 0.
        if trigger_idx > len(data) - half_width: 
             trigger_idx = 0
             
        # Scope Plot
        mid_y = height / 2
        
        pen = QPen(QColor(0, 255, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        
        points = []
        # Draw on left half (0 to half_width)
        # One pixel per sample if possible, or scale
        # block_size is 512. half_width might be 300.
        # Let's map samples 1:1 if possible for detail, or stretch.
        
        samples_to_show = min(len(data) - trigger_idx, half_width)
        
        for x in range(samples_to_show):
            val = data[trigger_idx + x]
            y = mid_y - (val * mid_y * 0.9)
            points.append((x, y))
            
        if len(points) > 1:
            for i in range(len(points) - 1):
                painter.drawLine(points[i][0], points[i][1], points[i+1][0], points[i+1][1])

        # Draw Spectrum (Right Half)
        # Compute FFT
        fft_data = np.abs(np.fft.rfft(data))
        # rfft size is block_size/2 + 1
        # Freq resolution = SampleRate / BlockSize = 44100 / 512 = 86 Hz
        # We want up to 10kHz.
        # Max freq is 22050. 10kHz is roughly half of that.
        # So we display first ~45% of FFT bins.
        
        n_bins = len(fft_data)
        max_bin = int(n_bins * (4000.0 / 22050.0))
        
        # Draw area
        painter.setBrush(QColor(0, 255, 0, 100)) # Green with alpha
        painter.setPen(Qt.NoPen)
        
        # Map bins to x (half_width to width)
        # Map mag to y (height to 0)
        
        poly_points = []
        poly_points.append(QPointF(half_width, height)) # Start bottom-left of right block
        
        if max_bin > 1:
            step_x = half_width / max_bin
            
            for i in range(max_bin):
                mag = fft_data[i]
                # Log scale for mag or linear? Linear is usually fine for simple view, but log is better for audio.
                # Let's use simple scaling first.
                # fft magnitude depends on signal level. 
                # Normalize?
                
                y = height - (mag * 4.0) # Scale factor increased 4x (0.5 -> 2.0)
                y = max(0, min(height, y))
                
                x = half_width + i * step_x
                poly_points.append(QPointF(x, y))
        
        poly_points.append(QPointF(width, height)) # End bottom-right
        
        painter.drawPolygon(poly_points)
        
        # Draw divider
        painter.setPen(QPen(QColor("#555")))
        painter.drawLine(half_width, 0, half_width, height)

class SynthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Analog Synth")
        self.resize(600, 600)
        
        # Audio Engine
        self.engine = AudioEngine()
        self.engine.start()
        
        # State
        self.current_module = "VCO1"
        self.knob_mappings = {
            "VCO1": [("Pitch", "pitch"), ("Wave", "wave"), ("Level", "level")],
            "VCF1": [("Cutoff", "cutoff"), ("Res", "res"), ("Env Amt", "env_amt")],
            "LFO1": [("Rate", "rate"), ("Wave", "wave"), ("Amt", "amt")],
            "EG1":  [("Attack", "attack"), ("Decay", "decay"), ("Release", "release")],
            
            "VCO2": [("Pitch", "pitch"), ("Wave", "wave"), ("Level", "level")],
            "VCF2": [("Cutoff", "cutoff"), ("Res", "res"), ("Env Amt", "env_amt")],
            "LFO2": [("Rate", "rate"), ("Wave", "wave"), ("Amt", "amt")],
            "EG2":  [("Attack", "attack"), ("Decay", "decay"), ("Release", "release")],
            
            "NOISE": [("Lvl Ch1", "pitch"), ("Type", "filt"), ("Lvl Ch2", "level")],
            "FX":    [("Time", "delay_time"), ("Fdbk", "feedback"), ("Mix", "mix")],
        }
        
        self.note_freqs = {
            "C1": 261.63, "D": 293.66, "E": 329.63, "F": 349.23,
            "G": 392.00, "A": 440.00, "B": 493.88, "C2": 523.25
        }
        
        self.active_notes = [] # Stack of active notes for last-note priority
        
        # Keyboard mapping
        self.key_map = {
            Qt.Key_Q: "C1", Qt.Key_W: "D", Qt.Key_E: "E", Qt.Key_R: "F",
            Qt.Key_A: "G", Qt.Key_S: "A", Qt.Key_D: "B", Qt.Key_F: "C2"
        }
        
        # UI Components
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)
        
        self.setup_knobs()
        self.setup_modules()
        
        # Oscilloscope
        self.scope = OscilloscopeWidget(self.engine)
        self.main_layout.addWidget(self.scope)
        
        self.setup_keyboard()
        
        # Initial Update
        self.update_knob_display()
        
        # Apply Styles
        self.apply_styles()

    def apply_styles(self):
        # Round buttons and fix resizing
        self.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                border: 2px solid #555;
                background-color: #eee;
                padding: 5px;
            }
            QPushButton:checked {
                background-color: #ccc;
            }
        """)

    def setup_knobs(self):
        # Top section: 3 Knobs with Labels and Value Display
        knob_container = QFrame()
        knob_container.setFrameShape(QFrame.StyledPanel)
        knob_layout = QHBoxLayout(knob_container)
        
        self.knobs = []
        self.knob_labels = []
        self.knob_values = []
        
        for i in range(3):
            v_layout = QVBoxLayout()
            
            lbl = QLabel(f"Param {i+1}")
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("font-weight: bold;")
            self.knob_labels.append(lbl)
            
            dial = QDial()
            dial.setRange(0, 1000) # 0.0 to 1.0 resolution
            dial.setValue(0)
            dial.setNotchesVisible(True)
            dial.valueChanged.connect(lambda val, idx=i: self.on_knob_change(idx, val))
            self.knobs.append(dial)
            
            val_lbl = QLabel("0.0")
            val_lbl.setAlignment(Qt.AlignCenter)
            self.knob_values.append(val_lbl)
            
            v_layout.addWidget(lbl)
            v_layout.addWidget(dial)
            v_layout.addWidget(val_lbl)
            knob_layout.addLayout(v_layout)
            
        self.main_layout.addWidget(knob_container)

    def setup_modules(self):
        # Grid of buttons
        grid_widget = QWidget()
        grid_layout = QGridLayout(grid_widget)
        
        modules = [
            ["VCO1", "VCF1", "LFO1", "EG1"],
            ["VCO2", "VCF2", "LFO2", "EG2"],
            [None, None, "NOISE", "FX"] # Adjusted layout to center noise/fx or put them somewhere
        ]
        
        self.module_buttons = []
        
        # Helper to create fixed size buttons
        def create_btn(name):
            btn = QPushButton(name)
            btn.setCheckable(True)
            btn.setFixedSize(60, 40) # Fix size to prevent resizing on bold
            return btn
        
        # Row 1
        for col, name in enumerate(modules[0]):
            btn = create_btn(name)
            btn.clicked.connect(lambda checked, n=name, b=btn: self.select_module(n, b))
            grid_layout.addWidget(btn, 0, col)
            self.module_buttons.append(btn)
            if name == self.current_module:
                btn.setChecked(True)
        
        # Row 2
        for col, name in enumerate(modules[1]):
            btn = create_btn(name)
            btn.clicked.connect(lambda checked, n=name, b=btn: self.select_module(n, b))
            grid_layout.addWidget(btn, 1, col)
            self.module_buttons.append(btn)

        # Row 3 (Noise, FX)
        btn_noise = create_btn("NOISE")
        btn_noise.clicked.connect(lambda c, n="NOISE", b=btn_noise: self.select_module(n, b))
        grid_layout.addWidget(btn_noise, 2, 1)
        self.module_buttons.append(btn_noise)
        
        btn_fx = create_btn("FX")
        btn_fx.clicked.connect(lambda c, n="FX", b=btn_fx: self.select_module(n, b))
        grid_layout.addWidget(btn_fx, 2, 2)
        self.module_buttons.append(btn_fx)

        
        self.module_btns_layout = grid_layout
        self.main_layout.addWidget(grid_widget)

    def setup_keyboard(self):
        kb_widget = QWidget()
        kb_layout = QHBoxLayout(kb_widget)
        
        self.note_buttons = {}
        notes = ["C1", "D", "E", "F", "G", "A", "B", "C2"]
        for note in notes:
            btn = QPushButton(note)
            btn.setFixedSize(60, 60) # Fix size to prevent resizing on bold
            # Use pressed/released for gate
            btn.pressed.connect(lambda n=note: self.key_press(n))
            btn.released.connect(self.key_release)
            kb_layout.addWidget(btn)
            self.note_buttons[note] = btn
            
        self.main_layout.addWidget(kb_widget)

    def select_module(self, name, btn):
        self.current_module = name
        
        # Radio button logic and styling
        for b in self.module_buttons:
            b.setChecked(False)
            b.setStyleSheet("") # Reset style
            
        btn.setChecked(True)
        btn.setStyleSheet("background-color: yellow; color: black; font-weight: bold;")
        
        self.update_knob_display()

    def get_display_value(self, param_key, value):
        # Format value based on parameter type
        if "pitch" in param_key:
             # Detune in octaves OR Noise Level Ch1
             if self.current_module == "NOISE":
                 return f"{value * 100:.0f} %"
             else:
                 detune = (value - 0.5) * 2.0
                 return f"{detune:+.2f} Oct"
        elif "cutoff" in param_key:
             # Exponential mapping display
             freq = 20.0 * (500.0 ** value)
             if freq > 1000:
                 return f"{freq/1000:.2f} kHz"
             return f"{int(freq)} Hz"
        elif "rate" in param_key:
             rate = value * 20.0
             return f"{rate:.2f} Hz"
        elif "time" in param_key:
             return f"{value * 1000:.0f} ms"
        elif "level" in param_key or "mix" in param_key or "amt" in param_key or "res" in param_key:
             return f"{value * 100:.0f} %"
        elif "attack" in param_key or "decay" in param_key or "release" in param_key:
             # Scale as in engine
             if "attack" in param_key: t = value * 2.0
             elif "decay" in param_key: t = value * 2.0
             else: t = value * 2.0
             return f"{t:.2f} s"
        elif "wave" in param_key:
             sel = int(value * 2.9)
             if sel == 0: return "Saw"
             elif sel == 1: return "Square"
             return "Sine"
        elif "filt" in param_key: # Noise Type
             if value < 0.45: return "Blue"
             elif value > 0.55: return "Pink"
             return "White"
        
        return f"{value:.2f}"

    def update_knob_display(self):
        mapping = self.knob_mappings[self.current_module]
        params = self.engine.params[self.current_module]
        
        for i in range(3):
            label_text, param_key = mapping[i]
            val = params[param_key]
            
            self.knob_labels[i].setText(label_text)
            
            # Block signals to prevent feedback loop
            self.knobs[i].blockSignals(True)
            self.knobs[i].setValue(int(val * 1000))
            self.knobs[i].blockSignals(False)
            
            # Update value label
            self.knob_values[i].setText(self.get_display_value(param_key, val))

    def on_knob_change(self, idx, val):
        mapping = self.knob_mappings[self.current_module]
        param_key = mapping[idx][1]
        
        # Update engine param
        float_val = val / 1000.0
        self.engine.params[self.current_module][param_key] = float_val
        
        # Update value label
        self.knob_values[idx].setText(self.get_display_value(param_key, float_val))

    def keyPressEvent(self, event):
        key = event.key()
        if not event.isAutoRepeat():
            if key in self.key_map:
                note = self.key_map[key]
                self.trigger_note_on(note)
    
    def keyReleaseEvent(self, event):
        key = event.key()
        if not event.isAutoRepeat():
            if key in self.key_map:
                note = self.key_map[key]
                self.trigger_note_off(note)

    def trigger_note_on(self, note):
        if note not in self.active_notes:
            self.active_notes.append(note)
            
        freq = self.note_freqs[note]
        self.engine.note_on(freq)
        
        self.update_keyboard_visuals()
        
    def trigger_note_off(self, note):
        if note in self.active_notes:
            self.active_notes.remove(note)
            
        freq = self.note_freqs[note]
        self.engine.note_off(freq)

        self.update_keyboard_visuals()

    def update_keyboard_visuals(self):
        # Update style for note buttons
        for btn in self.note_buttons.values():
            note = btn.text()
            if note in self.active_notes:
                 btn.setStyleSheet("background-color: yellow; color: black; font-weight: bold;")
            else:
                 btn.setStyleSheet("")

    def key_press(self, note):
        self.trigger_note_on(note)

    def key_release(self):
        # This is connected to released signal of button, but which button?
        # The lambda in setup_keyboard only passed note to pressed.
        # We need to know WHICH note was released if we want multi-touch via mouse?
        # Standard QPushButton released doesn't pass args. 
        # But we can capture sender.
        btn = self.sender()
        note = btn.text()
        self.trigger_note_off(note)

    def closeEvent(self, event):
        self.engine.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SynthWindow()
    window.show()
    sys.exit(app.exec())
