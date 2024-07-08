from pygame import mixer
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    mixer.init()
    mixer.music.load('./alarm.mp3')
    mixer.music.set_volume(1.0)   

    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f'{CLEAR_AND_RETURN} Alarm will sound in: {minutes_left:02d}: {seconds_left:02d}', end='', flush=True)
    
    mixer.music.play()
    print("Playing music...")

    # Keep the program running to allow the sound to play
    while mixer.music.get_busy():
        time.sleep(1)

minutes = int(input('How many minutes to wait: '))
seconds = int(input('How many seconds to wait: '))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)