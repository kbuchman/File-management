import pyscreenshot as sc
import pyautogui as gui
from pynput import mouse

# checking mouse status
def on_click(x, y, button, pressed):
    return True if pressed else False

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

def mouse_pos_scrap_vertical(left, rigth, margin_top, margin_bottom):
    while True:
        if listener:
            x, _ = gui.position()
            return left, 0 + margin_top, rigth, gui.size()[1] - margin_bottom

def main():
    take_screenshot(*mouse_pos_scrap_horizontal(50, 400, 200, 50)).show()

if __name__ == '__main__':
    main()