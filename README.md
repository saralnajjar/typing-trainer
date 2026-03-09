# Typing Trainer

A command line typing practice tool built in Python. Measures WPM and accuracy across three difficulty modes, and tracks your personal best scores locally.

## Features

- Three difficulty modes: Easy (common words), Medium (sentences), Hard (code snippets and symbols)
- WPM calculated using the standard 5-characters-per-word method
- Character-level accuracy scoring
- High score tracker saved to `scores.json`

## Setup

No dependencies beyond the Python standard library.
```bash
git clone https://github.com/saralnajjar/typing-trainer.git
cd typing-trainer
python3 main.py
```

Requires Python 3.10+.

## Usage

Run `python3 main.py` and select a difficulty from the menu. Press Enter when ready, type the prompt, and press Enter to submit. Your WPM, accuracy, and time are displayed after each round.
