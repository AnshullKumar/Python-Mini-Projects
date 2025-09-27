# Alarm Clock in Python
# ---------------------
# This project is a simple alarm clock built in Python that plays a sound after a user-defined countdown.
# Modules Used:
# ● time → For creating the countdown timer using sleep().
# ● playsound → For playing an MP3 file when the alarm goes off.


#Alarm-Fast-A1-www.fesliyanstudios.com.mp3

from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound(r"C:\CodeStuff💻\Python-Mini-Projects\Projects\Alarm.mp3")


minutes = int(input("How many minutes until the alarm runs out: "))
seconds = int(input("How many seconds until the alarm runs out: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)