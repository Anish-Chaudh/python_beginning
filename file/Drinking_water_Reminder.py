"""Exercise 11 - Drink Water Reminder (sound only, Windows)

Plays a sound and speaks "Time to drink water" out loud. No pop-ups.
Uses only the Python standard library and built-in Windows features.

Usage (Command Prompt or PowerShell):
    python water_reminder_sound.py            # every 60 minutes
    python water_reminder_sound.py 90         # every 90 minutes
    python water_reminder_sound.py 0.1        # test: every 6 seconds

Stop with Ctrl+C.
"""

import subprocess
import sys
import time
import winsound

SPOKEN_MESSAGE = "Hey Anish it's time to drink water!"
DEFAULT_INTERVAL_MINUTES = 60


def play_sound():
    """Play the Windows 'Exclamation' sound, then a short melody as a fallback."""
    try:
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    except RuntimeError:
        pass
    # A short rising melody: (frequency in Hz, duration in ms)
    for freq in (660, 880, 1100):
        winsound.Beep(freq, 250)


def speak(text):
    """Speak the message using Windows' built-in text-to-speech."""
    command = (
        "Add-Type -AssemblyName System.Speech; "
        "(New-Object System.Speech.Synthesis.SpeechSynthesizer)"
        f".Speak('{text}')"
    )
    try:
        subprocess.run(
            ["powershell", "-NoProfile", "-Command", command],
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
    except (OSError, subprocess.CalledProcessError):
        pass  # If speech is unavailable, the sound above is enough.


def remind():
    print(f"[{time.strftime('%H:%M')}] {SPOKEN_MESSAGE}")
    play_sound()
    speak(SPOKEN_MESSAGE)


def main():
    try:
        minutes = float(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INTERVAL_MINUTES
    except ValueError:
        print("Interval must be a number of minutes, e.g. 30")
        sys.exit(1)

    print(f"Water reminder started: every {minutes:g} minute(s). Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(minutes * 1)
            remind()
    except KeyboardInterrupt:
        print("\nReminder stopped. Stay hydrated!")


if __name__ == "__main__":
    main()
