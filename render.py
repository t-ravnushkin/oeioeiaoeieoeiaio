import cv2
from colorama import just_fix_windows_console
import os
from time import sleep
import pickle

just_fix_windows_console()


def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def background_colored(r, g, b, text):
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"


FPS = 25
FRAME_COUNT = 374
CONSOLE_WIDTH = 26 * 3


def cls():
    os.system("cls" if os.name == "nt" else "clear")


print("generating framestrings...")
framestrings = []
for frame_id in range(FRAME_COUNT):
    img = cv2.imread(f"other_small_frames/frame{frame_id}.png")
    curstr = ""
    for row in img:
        ind = 0
        for prepixel in row:
            pixel = prepixel.tolist()
            if pixel == [0, 0, 0]:
                # curstr += background_colored(0, 0, 0, " ")
                curstr += " "
                continue
            # color = find_closest_color(pixel)
            letter = "CAT"[ind % 3]
            ind += 1
            # curstr += colored(letter, color)
            b, g, r = pixel
            # curstr += background_colored(0, 0, 0, colored(r, g, b, letter))
            curstr += colored(r, g, b, letter)
        curstr += "\n"
    framestrings.append(curstr)

with open("framestrings.pickle", "wb") as f:
    pickle.dump(framestrings, f)

while True:
    for frame in framestrings:
        cls()
        print(frame)
        sleep(1 / FPS)
