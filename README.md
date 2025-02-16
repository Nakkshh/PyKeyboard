# PyKeyboard

A simple virtual piano using **Pygame** that allows you to play notes using your keyboard. This project provides an interactive way to play and visualize a piano on your computer screen.

## Features
- 🎹 **Play Notes**: Press keyboard keys to play piano sounds.
- 🎨 **Visual Feedback**: Keys change color when pressed.
- 🔊 **Smooth Sound Playback**: Multiple keys can be played in succession.
- 🎶 **Sustain Mode**: Hold `Shift` to sustain notes.

## Installation

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Install Dependencies
Run the following command to install the required dependencies:
```bash
pip install pygame
```

## Setup
1. Clone this repository or download the source files.
```bash
git clone https://github.com/your-username/PyKeyboard.git
cd PyKeyboard
```
2. Place the **.wav** sound files inside the `sounds/sounds_wav/` folder.
3. Run the program:
```bash
python main.py
```

## Controls
| Key  | Note  |
|------|------|
| A  | C4  |
| S  | D4  |
| D  | E4  |
| F  | F4  |
| G  | G4  |
| H  | A4  |
| J  | B4  |
| K  | C5  |
| W  | C#4  |
| E  | D#4  |
| T  | F#4  |
| Y  | G#4  |
| U  | A#4  |

### Special Features
- **Sustain Mode**: Press and hold `Shift` to sustain notes.
- **Stop Sound**: Release a key to stop sound (if sustain mode is off).

## Dependencies
- `pygame`
- `.wav` sound files for each piano note.

## Future Improvements
- 🎼 Add more octaves.
- 🎵 Implement recording and playback functionality.
- 🎚️ Add volume and sustain pedal controls.

## License
This project is open-source and available under the **MIT License**.

Happy Playing! 🎶

