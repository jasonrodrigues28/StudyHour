import time
import winsound

study_file = r"C:\Users\Jason\PycharmProjects\StudyHour\Audio Files\Study.wav"
rest_file = r"C:\Users\Jason\PycharmProjects\StudyHour\Audio Files\Take a break sound.wav"

study = 1800    #study for 30 min
rest = 900      #rest for 10 min

def study_audio():
    winsound.PlaySound(study_file, winsound.SND_FILENAME)

def rest_audio():
    winsound.PlaySound(rest_file, winsound.SND_FILENAME)

def start():
    for x in range(study, 0 ,-1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        print(f"{minutes:02}:{seconds:02}")
        time.sleep(1)
    rest_audio()

    print("rest")
    for x in range(rest, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        print(f"{minutes:02}:{seconds:02}")
        time.sleep(1)
    study_audio()

while True:
    start()
