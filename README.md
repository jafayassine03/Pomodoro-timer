🍅 Terminal Pomodoro Timer (Python)

A clean, minimal, and distraction-free Pomodoro timer that runs directly in your terminal.

Built using pure Python (standard library only) — no external dependencies.
Designed for developers, students, and anyone who wants deep focus without bloated apps.

🚀 Features

⏳ Customizable work, short break, and long break durations

🔁 Automatic long break after every 4 focus sessions

📊 Real-time countdown timer (updates every second)

██████████ Visual progress bar inside the terminal

🔔 Sound notification when a session ends

🛑 Graceful exit with Ctrl + C

🖥 Automatic terminal screen clearing between sessions

♾ Infinite focus loop (runs until manually stopped)

💻 Cross-platform support (Windows, macOS, Linux)

⚙️ Input validation with fallback to default values

🧠 How It Works

This timer follows the classic Pomodoro Technique:

Focus for 25 minutes

Take a 5-minute short break

Repeat for 4 sessions

After 4 sessions → take a 15-minute long break

Continue the cycle

The loop runs continuously to keep you in deep work mode without interruptions.

📦 Installation

Make sure you have Python 3 installed.

Clone the repository:

git clone https://github.com/yourusername/terminal-pomodoro.git
cd terminal-pomodoro

Run the script:

python pomodoro.py

That’s it. No setup. No dependencies.

🎯 Why This Project?

Most Pomodoro apps are:

Bloated

Distracting

Full of UI clutter

This project focuses on:

✔ Simplicity
✔ Performance
✔ Zero dependencies
✔ Terminal-based productivity

Perfect for developers who live in the command line.

🛠 Tech Stack

Python 3

Standard Library:

time

os

sys

No third-party packages required.

📁 Project Structure
terminal-pomodoro/
│
├── pomodoro.py
└── README.md

Simple. Clean. Maintainable.

🔮 Possible Future Improvements

Session statistics tracking

Daily productivity report

Save session history to file

Dark-mode ASCII UI enhancements

Packaging as a CLI tool (pip install)

Optional GUI version
