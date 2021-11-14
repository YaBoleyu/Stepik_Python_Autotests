import win32api, win32con
import time
import pyautogui
import random

def click_win32(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,x,y,0,0)


def click_pyautogui(x,y):
    pyautogui.moveRel(x,y,0,0)
    pyautogui.doubleClick() 

def timer():
    timing = time.time()
    
    while True:
        if time.time()-timing > 10.0:
            timing =time.time()
            RandomNumber =random.randint(1,255)
            click_pyautogui(RandomNumber,-1)
            print("5 seconds \n "+str(RandomNumber))
            time.sleep(5)
            RandomNumber_2 = RandomNumber*-1
            click_pyautogui(RandomNumber_2,1)
            print("10 sec \n "+str(RandomNumber_2))

timer()