from colorama import just_fix_windows_console
from termcolor import colored

just_fix_windows_console()
colors = [
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "light_grey",
    "dark_grey",
    "light_red",
    "light_green",
    "light_yellow",
    "light_blue",
    "light_magenta",
    "light_cyan",
]
for color in colors:
    print(color, colored("CAT", color))
