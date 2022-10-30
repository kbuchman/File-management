from multiprocessing.connection import Listener
from turtle import onclick
import pyscreenshot as sc
import pyautogui as gui
from pynput import mouse

def on_click(x, y, button, pressed):
    if not pressed:
        return False
    return True

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

def take_screenshot(xs, ys, xe, ye):
    screen = sc.grab((xs, ys, xe, ye))
    return screen

def mouse_pos_scrap_horizontal(margin_left, margin_rigth, top, bottom):
    while True:
        if listener:
            _, y = gui.position()
            return 0 + margin_left, y - top, gui.size()[0] - margin_rigth, y + bottom

def main():

    take_screenshot(*mouse_pos_scrap_horizontal(50, 400, 200, 50)).show()

if __name__ == '__main__':
    main()