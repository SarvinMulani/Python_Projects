from colorama import Fore
import time
# import playsound

print(Fore.YELLOW + '')

# ANSI
CLEAR = '\033[2J'
CLEAR_AND_REPLACE = '\033[H'

def alarm(seconds):
    time_passed = 0
    
    print(CLEAR)
    while time_passed < seconds:
        time.sleep(1)
        time_passed += 1
        
        time_left = seconds - time_passed
        minute_left = time_left // 60
        second_left = time_left % 60
        
        print(f"{CLEAR_AND_REPLACE}{minute_left:02d}:{second_left:02d}")
    # playsound('mixkit-alarm-digital-clock-beep-989.wav')

duration = int(input(Fore.BLUE + "Timer(sec): "))
alarm(duration)