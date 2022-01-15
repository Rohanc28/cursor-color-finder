import pyautogui
import time

print("- - - - - ")
try:
    while True:
        x,y=pyautogui.position()
        time.sleep(0.5)
        pyautogui.displayMousePosition()
        print("- - - - - ")
        
except:
    KeyboardInterrupt()
    print('\n')
    
