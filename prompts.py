import random

EASY = [
    "the cat sat on the mat",
    "dogs run fast in the park",
    "she sells sea shells",
    "a big red bus",
    "jump over the fence",
    "open the blue door",
    "the sun set at six",
    "cold wind blew all night",
]

MEDIUM = [
    "the quick brown fox jumps over the lazy dog",
    "practice makes perfect when you commit to it daily",
    "keyboard shortcuts can save you hours every week",
    "version control is an essential skill for every developer",
    "reading documentation is underrated but incredibly useful",
    "clean code is easier to debug than clever code",
]

HARD = [
    "encrypt(key=0x3F, mode='CBC') -> bytes | None",
    "for i, (key, val) in enumerate(data.items()): print(f'{i}: {key} = {val}')",
    "git commit -m 'fix: resolve merge conflict in auth module (#42)'",
    "SELECT * FROM users WHERE created_at > '2025-01-01' ORDER BY name ASC;",
    "raise ValueError(f'expected int, got {type(x).__name__}: {x!r}')",
]

MODES = {
    "1": ("Easy", EASY),
    "2": ("Medium", MEDIUM),
    "3": ("Hard", HARD),
}


def get_prompt(mode_key: str) -> str:
    _, prompts = MODES[mode_key]
    return random.choice(prompts)
