import time
import os
import sys
import random
from datetime import datetime

DEFAULT_WORK = 25 * 60
DEFAULT_SHORT_BREAK = 5 * 60
DEFAULT_LONG_BREAK = 15 * 60
SESSIONS_BEFORE_LONG = 4
DAILY_GOAL = 6  
STATS_FILE = "stats.txt"

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def beep():
    if os.name == "nt":
        import winsound
        winsound.Beep(1000, 500)
    else:
         print("\a", end="")


def load_stats():
    if not os.path.exists(STATS_FILE):
        return {"sessions": 0, "focus_time": 0}

    with open(STATS_FILE, "r") as f:
        lines = f.readlines()
        return {
            "sessions": int(lines[0].strip()),
            "focus_time": int(lines[1].strip())
        }


def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        f.write(f"{stats['sessions']}\n")
        f.write(f"{stats['focus_time']}\n")


def motivational_quote():
    quotes = [
        "Small progress is still progress.",
        "Discipline beats motivation.",
        "Stay focused. Stay dangerous.",
        "Success is built in sessions.",
        "One session closer to your goals."
    ]
    return random.choice(quotes)



def countdown(seconds, label):
    total_time = seconds
    paused = False

    try:
        while seconds:
            mins = seconds // 60
            secs = seconds % 60
            timer = f"{mins:02d}:{secs:02d}"

            progress = int((1 - seconds / total_time) * 20)
            bar = "█" * progress + "-" * (20 - progress)

            print(f"{label} | {timer} | [{bar}] (P = Pause)", end="\r")

            time.sleep(1)
            seconds -= 1

            if os.name == "nt":
                import msvcrt
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode("utf-8").lower()
                    if key == "p":
                        paused = not paused
                        while paused:
                            print("\nPaused. Press P to resume.", end="\r")
                            time.sleep(0.5)
                            if msvcrt.kbhit():
                                key = msvcrt.getch().decode("utf-8").lower()
                                if key == "p":
                                    paused = False

        print(f"\n{label} finished! 🔔")
        beep()

    except KeyboardInterrupt:
        print("\nSession stopped.")
        sys.exit()


def pomodoro():
    stats = load_stats()
    session = 0

    while True:
        clear()
        print("==== 🚀 POMODORO PRO ====\n")
        print("1. Start Focus Session")
        print("2. View Stats")
        print("3. Reset Stats")
        print("4. Exit\n")

        choice = input("Select option: ")

        if choice == "1":
            session += 1
            clear()
            print(f"Session {session} - Focus Time 💻\n")

            countdown(DEFAULT_WORK, "Work")

            stats["sessions"] += 1
            stats["focus_time"] += DEFAULT_WORK
            save_stats(stats)

            print("\n" + motivational_quote())
            time.sleep(2)

            if session % SESSIONS_BEFORE_LONG == 0:
                clear()
                print("Time for a LONG break 🛋️\n")
                countdown(DEFAULT_LONG_BREAK, "Long Break")
            else:
                clear()
                print("Time for a short break ☕\n")
                countdown(DEFAULT_SHORT_BREAK, "Short Break")

        elif choice == "2":
            clear()
            total_minutes = stats["focus_time"] // 60
            print("==== 📊 YOUR STATS ====\n")
            print(f"Total Sessions: {stats['sessions']}")
            print(f"Total Focus Time: {total_minutes} minutes")

            if stats["sessions"] >= DAILY_GOAL:
                print("\n🎯 Daily goal achieved! You're on fire!")
            else:
                print(f"\nSessions until goal: {DAILY_GOAL - stats['sessions']}")

            input("\nPress Enter to return...")

        elif choice == "3":
            stats = {"sessions": 0, "focus_time": 0}
            save_stats(stats)
            print("Stats reset successfully.")
            time.sleep(1)

        elif choice == "4":
            print("Stay productive. See you next session 👊")
            sys.exit()

        else:
            print("Invalid option.")
            time.sleep(1)


if __name__ == "__main__":
    pomodoro()