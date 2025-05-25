import time
import winsound
import threading

study_file = r"C:\Users\Jason\PycharmProjects\StudyHour\Audio Files\Study.wav"
rest_file = r"C:\Users\Jason\PycharmProjects\StudyHour\Audio Files\Take a break sound.wav"

study = 1800  # study for 30 min (1800 seconds)
rest = 900    # rest for 15 min (900 seconds)

def study_audio():
    winsound.PlaySound(study_file, winsound.SND_FILENAME)

def rest_audio():
    winsound.PlaySound(rest_file, winsound.SND_FILENAME)

def countdown(duration):
    for x in range(duration, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        print(f"{minutes:02}:{seconds:02}")
        time.sleep(1)

def start():
    # Start study audio in a separate thread
    study_thread = threading.Thread(target=study_audio)
    study_thread.start()

    # Start study timer
    countdown(study)

    print("rest")

    # Start rest audio in a separate thread
    rest_thread = threading.Thread(target=rest_audio)
    rest_thread.start()

    # Start rest timer
    countdown(rest)

while True:
    start()
