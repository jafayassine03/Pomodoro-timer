import time
import os

WORK_TIME = 25 * 60        
SHORT_BREAK = 5 * 60       
LONG_BREAK = 15 * 60       
SESSIONS_BEFORE_LONG = 4


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def countdown(seconds, label):
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{mins:02d}:{secs:02d}"
        print(f"{label} | {timer}", end="\r")
        time.sleep(1)
        seconds -= 1

    print(f"\n{label} finished! 🔔")


def pomodoro():
    session = 0

    while True:
        session += 1
        clear()
        print(f"Session {session} - Focus Time 💻")
        countdown(WORK_TIME, "Work")

        if session % SESSIONS_BEFORE_LONG == 0:
            print("\nTime for a long break 🛋️")
            countdown(LONG_BREAK, "Long Break")
        else:
            print("\nTime for a short break ☕")
            countdown(SHORT_BREAK, "Short Break")


if __name__ == "__main__":
    pomodoro()