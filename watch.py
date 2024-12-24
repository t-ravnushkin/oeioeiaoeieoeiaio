import pickle
from time import sleep
import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


FPS = 25
FRAME_COUNT = 374
CONSOLE_WIDTH = 26 * 3

framestrings = []

with open("framestrings.pickle", "rb") as f:
    framestrings = pickle.load(f)

while True:
    for frame in framestrings:
        print(frame)
        sleep(1 / FPS)
        cls()
