import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

CONSOLE_WIDTH =26 * 3
CONSOLE_HEIGHT = 15 * 3

table1 = [["A" for i in range(CONSOLE_WIDTH)] for j in range(CONSOLE_HEIGHT)]
table2 = [["B" for i in range(CONSOLE_WIDTH)] for j in range(CONSOLE_HEIGHT)]

for i in range(100000):
    time.sleep(1 / 25)
    cls()
    if i % 2 == 0:
        for row in table1:
            print("".join(row))
    else:
        for row in table2:
            print("".join(row))
