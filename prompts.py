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
    "the juxtaposition of ephemeral and permanent is paradoxical",
    "ambiguity, though frustrating, is often deliberately cultivated",
    "the archaeologist meticulously catalogued every artefact",
    "conscientious, diligent, and tenacious — three underrated virtues",
    "the bureaucratic labyrinth was, unsurprisingly, impenetrable",
    "melancholy persists; clarity, however, remains elusive",
    "the phenomenon was neither unprecedented nor wholly inexplicable",
    "verbose, convoluted prose obscures rather than illuminates meaning",
]

MODES = {
    "1": ("Easy", EASY),
    "2": ("Medium", MEDIUM),
    "3": ("Hard", HARD),
}


def get_prompt(mode_key: str) -> str:
    _, prompts = MODES[mode_key]
    return random.choice(prompts)
