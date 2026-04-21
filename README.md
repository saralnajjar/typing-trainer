# Typing Trainer

A command line typing practice tool built in Python. Measures WPM and accuracy across three difficulty modes, and tracks personal best scores locally.

## Features

- Three difficulty modes: Easy (common words), Medium (sentences), Hard (code snippets and symbols)
- Timer starts on first keypress
- WPM calculated using the standard 5-characters-per-word method
- Character-level accuracy scoring
- High score tracker and stats saved to `scores.json`
- `--mode` flag to skip the menu and start immediately

## Setup

```bash
git clone https://github.com/saralnajjar/typing-trainer.git
cd typing-trainer
python3 main.py
```

## Usage

Run `python3 main.py` and select a difficulty from the menu. Start typing when the prompt appears. Timer begins on your first keypress. WPM, accuracy, and time are shown after each round.

To skip the menu:

```bash
python3 main.py --mode easy
python3 main.py --mode medium
python3 main.py --mode hard
```