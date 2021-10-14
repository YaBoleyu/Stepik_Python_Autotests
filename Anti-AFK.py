import win32api, win32con
import time
import pyautogui

def click_win32(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,x,y,0,0)

def click_pyautogui(x,y):
    pyautogui.moveRel(x,y,0,0)
    

def timer():
    timing = time.time()
    while True:
        if time.time()-timing > 10.0:
            timing =time.time()
            click_pyautogui(255,0)
            print("5 seconds")
            time.sleep(5)
            click_pyautogui(-255,0)
            print("10 sec")

timer();