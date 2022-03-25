from pynput.mouse import Listener
import logging

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
liste=[]
def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    if pressed:
        print(x,y)
        liste.append([x,y])

def on_scroll(x, y, dx, dy):
    pass

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
