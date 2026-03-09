import time


def run_test(prompt: str) -> dict:
    print("\n" + "─" * 60)
    print("TYPE THE FOLLOWING:")
    print(f"\n  {prompt}\n")
    print("─" * 60)
    print("Press Enter when ready, then start typing...")
    input()

    print(f"\n  {prompt}\n")
    start = time.time()
    typed = input("> ")
    end = time.time()

    elapsed = end - start
    wpm = calculate_wpm(typed, elapsed)
    accuracy = calculate_accuracy(prompt, typed)

    return {
        "wpm": wpm,
        "accuracy": accuracy,
        "elapsed": round(elapsed, 2),
        "prompt": prompt,
        "typed": typed,
    }


def calculate_wpm(typed: str, elapsed_secs: float) -> float:
    if elapsed_secs <= 0:
        return 0.0
    words = len(typed) / 5
    minutes = elapsed_secs / 60
    return round(words / minutes, 1)


def calculate_accuracy(original: str, typed: str) -> float:
    if not original:
        return 0.0
    correct = sum(1 for a, b in zip(original, typed) if a == b)
    total = max(len(original), len(typed))
    return round((correct / total) * 100, 1)
