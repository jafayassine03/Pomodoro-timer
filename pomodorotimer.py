import time
import os
import sys
import random
import json
from datetime import datetime, date

DEFAULT_WORK = 25 * 60
DEFAULT_SHORT_BREAK = 5 * 60
DEFAULT_LONG_BREAK = 15 * 60
SESSIONS_BEFORE_LONG = 4
DAILY_GOAL = 6

STATS_FILE = "stats.json"



def clear():
    os.system("cls" if os.name == "nt" else "clear")


def beep():
    if os.name == "nt":
        import winsound
        winsound.Beep(1000, 400)
    else:
        print("\a", end="")


def motivational_quote():
    quotes = [
        "Small progress is still progress.",
        "Discipline beats motivation.",
        "Stay focused. Stay dangerous.",
        "Success is built in sessions.",
        "One session closer to your goals.",
        "Consistency creates champions.",
        "Lock in. Level up."
    ]
    return random.choice(quotes)



def load_stats():
    if not os.path.exists(STATS_FILE):
        return {
            "sessions": 0,
            "focus_time": 0,
            "last_date": str(date.today()),
            "streak": 0
        }

    with open(STATS_FILE, "r") as f:
        return json.load(f)


def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)


def reset_if_new_day(stats):
    today = str(date.today())

    if stats["last_date"] != today:
        if stats["sessions"] >= DAILY_GOAL:
            stats["streak"] += 1
        else:
            stats["streak"] = 0

        stats["sessions"] = 0
        stats["focus_time"] = 0
        stats["last_date"] = today



def countdown(seconds, label):
    total_time = seconds

    try:
        while seconds:
            mins = seconds // 60
            secs = seconds % 60
            timer = f"{mins:02d}:{secs:02d}"

            progress = int((1 - seconds / total_time) * 25)
            bar = "█" * progress + "-" * (25 - progress)

            now = datetime.now().strftime("%H:%M:%S")

            print(f"{label} | {timer} | [{bar}] | {now}", end="\r")

            time.sleep(1)
            seconds -= 1

        print(f"\n{label} finished! 🔔")
        beep()

    except KeyboardInterrupt:
        print("\nSession stopped.")
        sys.exit()



def pomodoro():
    stats = load_stats()
    reset_if_new_day(stats)
    save_stats(stats)

    session = 0

    while True:
        clear()
        print("==== 🚀 POMODORO PRO X ====\n")
        print("1. Start Focus Session")
        print("2. Custom Focus Time")
        print("3. View Stats")
        print("4. Reset Stats")
        print("5. Exit\n")

        choice = input("Select option: ")

        if choice == "1":
            work_time = DEFAULT_WORK

        elif choice == "2":
            try:
                minutes = int(input("Enter focus time (minutes): "))
                work_time = minutes * 60
            except:
                print("Invalid input.")
                time.sleep(1)
                continue

        elif choice == "3":
            clear()
            total_minutes = stats["focus_time"] // 60
            print("==== 📊 YOUR STATS ====\n")
            print(f"Today's Sessions: {stats['sessions']}")
            print(f"Today's Focus Time: {total_minutes} minutes")
            print(f"🔥 Current Streak: {stats['streak']} days")

            if stats["sessions"] >= DAILY_GOAL:
                print("\n🎯 Daily goal achieved! You're on fire!")
            else:
                print(f"\nSessions until goal: {DAILY_GOAL - stats['sessions']}")

            input("\nPress Enter to return...")
            continue

        elif choice == "4":
            stats = {
                "sessions": 0,
                "focus_time": 0,
                "last_date": str(date.today()),
                "streak": 0
            }
            save_stats(stats)
            print("Stats reset.")
            time.sleep(1)
            continue

        elif choice == "5":
            print("Stay productive. See you next session 👊")
            sys.exit()

        else:
            print("Invalid option.")
            time.sleep(1)
            continue

        
        session += 1
        clear()
        print(f"Session {session} - Focus Time 💻\n")

        countdown(work_time, "Work")

        stats["sessions"] += 1
        stats["focus_time"] += work_time
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


if __name__ == "__main__":
    pomodoro()