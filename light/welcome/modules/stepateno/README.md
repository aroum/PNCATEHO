# Техническое Задание: Синтезатор/Секвенсор на базе RP2040

## 1. Аппаратная конфигурация (Hardware)

- **Микроконтроллер:** Raspberry Pi RP2040 (16 МБ Flash).

- **Устройства ввода:**

- 10 тактовых кнопок: `K1-K10` (Pins 1-10).

- 1 инкрементальный энкодер с нажатием: `E1` (Pins 18, 19). [Ali](https://aliexpress.ru/item/1005009018396383.html) и [другой вариант](https://aliexpress.ru/item/1005006127287538.html)  и [еще](https://aliexpress.ru/item/1005001964120854.html)

- 3 аналоговых потенциометра: `P1, P2, P3` (Pins 15, 16, 17). [Ali](https://aliexpress.ru/item/1005005956593595.html)

- **Индикация:**

- 10 светодиодов SK6812 RGB (Pin 11), расположенных под каждой кнопкой.

- **Интерфейсы:**

- 1x MIDI Jack In: `Pins 12`. [Ali](https://aliexpress.ru/item/4001051534120.html)

- 1x MIDI Jack Out: `Pins 13`. [Ali](https://aliexpress.ru/item/4001051534120.html)

- 1x Audio Jack Out: `Pin 14` (+ внешний RC-фильтр).  [Ali](https://aliexpress.ru/item/4001051534120.html)

- 1x USB порт (MIDI Device Class).

### Расположение органов управления

```
[ E1 ] 
[ P1 ] [ P2 ] [ P3 ]

[ K1 ] [ K2 ] [ K3 ] [ K4 ]
[ K5 ] [ K6 ] [ K7 ] [ K8 ]
                     [ K9 ] [ K10 ]
```

## 2. Общая логика управления

### Защита значений (Catch-up Mode)

При переключении режимов (например, из Synth в Seq) физическое положение потенциометра может не совпадать с программным значением параметра.

- Новое значение применяется только тогда, когда пользователь сдвинул потенциометр на величину, превышающую порог дребезга (dead-zone), и "пересек" сохраненное значение параметра.

## 3. Режимы работы

### 3.1. Режим настроек (Settings)

**Вход/Выход:** Удерживать `K8 + K9 + K10` в течение 2 секунд. Параметры сохраняются во Flash-памяти при выходе.

- `K1`: Переключение USB MIDI (In/Out/Both). Индикация цветом.

- `K2`: Переключение Jack MIDI (In/Out/Off). Индикация цветом.

- `K3`: Глобальный режим по умолчанию (Synth/Sequencer).

- `K5`: Выбор MIDI-канала для USB (перебор 1-16).

- `K6`: Выбор MIDI-канала для Jack (перебор 1-16).

- _Примечание:_ При выборе каналов светодиоды `K1-K8` показывают номер канала двоичным кодом или цветом.

### 3.2. Режим Синтезатора (Synth)

#### Регулировки (Потенциометры)

1. **Cutoff:** Частота среза фильтра.

2. **Resonance:** Резонанс фильтра.

3. **Envelope Amount:** Глубина влияния огибающей.

#### Регулировки (Энкодер)

- `E1`: Переключение пресетов звука.

- `Chord (K8) + E1`: Attack / Release (баланс или по очереди).

- `fn1 (K9) + E1`: Выбор формы волны (Saw, Square, Sine, Noise).

- `fn2 (K10) + E1`: Velocity (чувствительность нажатия).

- `fn1 + fn2 + E1`: Общая громкость Audio Out.

#### Клавиатура и модификаторы

- `K1 - K7`: Ноты До, Ре, Ми, Фа, Соль, Ля, Си.

- `K8 (Chord)`: Переключение режима (Single note / Chord).

- `fn1 + Нота`: Понижение на полтона (Flat).

- `fn2 + Нота`: Повышение на полтона (Sharp).

- `Chord + fn1`: Октава вниз.

- `Chord + fn2`: Октава вверх.

### 3.3. Режим Степ-Секвенсора (Step Sequencer)

Поддерживает до 32 шагов (4 страницы по 8 шагов).

- **Индикация страниц:** Светодиоды `K9` и `K10` показывают номер текущей страницы цветом или комбинацией.

#### Состояние: seq_play (Воспроизведение)

- `K1 - K8`: Вкл/Выкл (Mute) шага. Mute = Фиолетовый LED.

- `K(x) + fn1`: Установка флага **STOP**. Секвенция сбрасывается в начало после этого шага. LED горит постоянно выбранным цветом. (это шаг не воспроизводится)

- `fn1`: Предыдущая страница.

- `fn2`: Следующая страница.

- **Потенциометры:**

1. **BPM:** Темп воспроизведения.

2. **Swing:** Смещение четных шагов (грув).

3. **Probability:** Вероятность срабатывания активного шага (0-100%).

- **Энкодер:**

- `E1`: **Gate Length:** Длительность всех нот в секвенции.

- `Chord + E1`: Transpose (Транспонирование всей последовательности).

- `fn1 + E1`: Режим хода (Forward, Reverse, Random, Ping-pong).

- `fn2 + E1`: Note Length (Индивидуальная кратность шага).

- `fn1 + fn2 + E1`: Громкость.

#### Состояние: seq_edit (Редактирование структуры)

Переход: Короткое нажатие `fn1 + fn2` в режиме воспроизведения.

- `K1 - K8`: Выбор шага для редактирования (переход в `step_edit`).

- `fn1 + K(x)`: Быстрый Mute шага.

- `fn2 + K(x)`: Stop шаг.

- `fn1 / fn2`: Навигация по страницам.

#### Состояние: step_edit (Редактирование конкретного шага)

Активируется при выборе шага в `seq_edit`.

- Интерфейс полностью повторяет режим **Synth**.

- Пользователь настраивает звук, ноту и параметры для конкретного шага.

- `fn1 + fn2`: **Save & Exit**. Параметры записываются в шаг, возврат в `seq_edit`.

## 4. Световая индикация

- **Synth:** Клавиши светятся мягким белым, при нажатии — цвет пресета.

- **Sequencer:**

- Слой 1 (1-8): Синий.

- Слой 2 (9-16): Зеленый.

- Слой 3 (17-24): Желтый.

- Слой 4 (25-32): Красный.

- **Running Light:** Белый яркий курсор поверх текущего шага.

## 5. Программные требования

1. Использование **Core 1** для генерации звука (PWM 12-bit+, Fs = 44.1kHz).

2. Использование **Core 0** для обработки прерываний энкодера, кнопок и MIDI-стека.

3. Реализация антидребезга (Debounce) для кнопок — 5 мс.

4. Сглаживание данных с потенциометров (экспоненциальное скользящее среднее).

----

## picokorpe

| selector pos | knob a         | knob b        |
| ------------ | -------------- | ------------- |
| 1            | sample         | break         |
| 2            | filter         | stretch       |
| 3            | gate           | gate prob.    |
| 4            | jump prob.     | retrig prob.  |
| 5            | tunnel prob.   | reverse prob. |
| 6            | sequencer rec. | sequencer on  |
| 7            | save           | load          |
| 8            | volume/fold    | tempo         |
sample changes the sample being played (holds >100 samples totaling ~8 minutes).
break modifies all probabilities simultaneously using varied easing functions.
filter is a resonant low-pass filter that attenuates higher frequencies.
stretch performs a lofi timestretch effect.
gate controls the amount of gating on the sample.
gate prob. controls the probability of gating.
jump prob. controls the likelihood of jumping to a different step in the current sample.
retrig prob. controls the likehood of retriggering.
tunnel prob. controls the likelihood of jumping to a different sample.
reverse prob. controls the probability of reversing direction.
sequencer rec will record sequences, up to 128 steps (cw = record, ccw = erase).
sequencer on turns on the sequencer (cw = on, ccw = off).
save saves probabilities, sample, volume, and tempo (cw = save).
load recalls the last save (cw = load).
volume/fold changes the volume and adds a wavefolding effect.
tempo controls the tempo in steps of 5 bpm (50-305), encoded in binary.

<https://infinitedigits.co/docs/products/pikocore/>
