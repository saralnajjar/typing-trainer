import time
import sys
import tty
import termios

def run_test(prompt: str) -> dict:
    print("\n" + "─" * 60)
    print("TYPE THE FOLLOWING:")
    print(f"\n  {prompt}\n")
    print("─" * 60)
    print("Start typing to begin...\n> ", end="", flush=True)

    typed = ""
    start = None

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)

            # ctrl+c
            if ch == "\x03":
                raise KeyboardInterrupt

            # enter
            if ch in ("\r", "\n"):
                break

            # backspace
            if ch in ("\x7f", "\x08"):
                if typed:
                    typed = typed[:-1]
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
                continue

            if start is None:
                start = time.time()

            typed += ch
            sys.stdout.write(ch)
            sys.stdout.flush()

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    end = time.time()
    print()

    if start is None:
        start = end

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