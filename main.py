from engine import run_test
from prompts import get_prompt, MODES
from scores import save_score, show_high_scores, show_stats


def print_banner():
    print("\n" + "═" * 60)
    print("  TYPING TRAINER")
    print("═" * 60)


def select_difficulty() -> tuple:
    print("\n  Select difficulty:")
    for key, (name, _) in MODES.items():
        print(f"    {key}. {name}")
    print("    4. View high scores")
    print("    5. Stats")
    print("    6. Quit")

    while True:
        choice = input("\n> ").strip()
        if choice in MODES:
            return choice, MODES[choice][0]
        elif choice == "4":
            return "4", "scores"
        elif choice == "5":
            return "5", "stats"
        elif choice == "6":
            return "6", "quit"
        else:
            print("  Please enter 1–6.")


def print_results(result: dict) -> None:
    print("\n" + "─" * 60)
    print("  RESULTS")
    print("─" * 60)
    print(f"  WPM:      {result['wpm']}")
    print(f"  Accuracy: {result['accuracy']}%")
    print(f"  Time:     {result['elapsed']}s")
    print("─" * 60)


def main():
    print_banner()

    while True:
        mode_key, difficulty = select_difficulty()

        if difficulty == "quit":
            print("\n  See you next time!\n")
            break
        elif difficulty == "scores":
            show_high_scores()
            continue
        elif difficulty == "stats":
            show_stats()
            continue

        prompt = get_prompt(mode_key)
        result = run_test(prompt)
        print_results(result)
        save_score(result, difficulty)

        again = input("\n  Go again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  See you next time!\n")
            break


if __name__ == "__main__":
    main()