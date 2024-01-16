import time
import pyautogui
import keyboard

def scroll_to_top():
    pyautogui.keyDown('ctrl')
    pyautogui.press('home')
    time.sleep(0.1)
    pyautogui.keyUp('ctrl')

# Run the function to scroll to the top

while True:
    if keyboard.is_pressed('q'):
        print("Script stopped by user.")
        break

    scroll_to_top()