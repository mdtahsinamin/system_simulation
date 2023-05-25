import random

import numpy as np

num = 20
total_win = 0
total_cost = 0
for i in range(num):
    print("Game :", i)
    tails = 0
    head = 0
    cnt = 0
    while 1:
        rn = random.randint(0, 9)
        cnt += 1
        total_cost += 1
        if rn >= 0 and rn <= 4:
            head += 1
        elif rn >= 5 and rn <= 9:
            tails += 1

        if (abs(head - tails) >= 3):
            break

    if (abs(head - tails) >= 3 and cnt < 8):
        print("You win")
        total_win += 8
    else:
        print("You loss")

print(total_win)
print(total_cost)
