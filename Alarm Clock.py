import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm has been set to {alarm_time}")
    sound_file = "Alarm_Music/Unlike Pluto - Time Is Eating [NCS Release].mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("It's time to wake up! 🌄")
            is_running = False

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = (input("Set your alarm (HH: MM: SS:): "))
    set_alarm(alarm_time)
