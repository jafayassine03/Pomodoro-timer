import time
import os
import sys

DEFAULT_WORK = 25 * 60
DEFAULT_SHORT_BREAK = 5 * 60
DEFAULT_LONG_BREAK = 15 * 60
SESSIONS_BEFORE_LONG = 4


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def beep():
    if os.name == "nt":
        import winsound
        winsound.Beep(1000, 500)
    else:
        print("\a", end="")


def countdown(seconds, label):
    try:
        while seconds:
            mins = seconds // 60
            secs = seconds % 60
            timer = f"{mins:02d}:{secs:02d}"

            progress = int((1 - seconds / total_time) * 20)
            bar = "█" * progress + "-" * (20 - progress)

            print(f"{label} | {timer} | [{bar}]", end="\r")
            time.sleep(1)
            seconds -= 1

        print(f"\n{label} finished! 🔔")
        beep()

    except KeyboardInterrupt:
        print("\nSession stopped by user.")
        sys.exit()


def get_custom_time(prompt, default):
    try:
        value = input(f"{prompt} (minutes, default {default//60}): ")
        if value.strip() == "":
            return default
        return int(value) * 60
    except ValueError:
        print("Invalid input. Using default.")
        return default


def pomodoro():
    global total_time

    clear()
    print("==== POMODORO TIMER ====\n")

    work_time = get_custom_time("Work time", DEFAULT_WORK)
    short_break = get_custom_time("Short break", DEFAULT_SHORT_BREAK)
    long_break = get_custom_time("Long break", DEFAULT_LONG_BREAK)

    session = 0

    while True:
        session += 1
        clear()
        print(f"Session {session} - Focus Time 💻\n")

        total_time = work_time
        countdown(work_time, "Work")

        if session % SESSIONS_BEFORE_LONG == 0:
            print("\nTime for a LONG break 🛋️\n")
            total_time = long_break
            countdown(long_break, "Long Break")
        else:
            print("\nTime for a short break ☕\n")
            total_time = short_break
            countdown(short_break, "Short Break")


if __name__ == "__main__":
    pomodoro()