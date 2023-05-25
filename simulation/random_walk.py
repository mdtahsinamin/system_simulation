import numpy as np
import matplotlib.pyplot as plt

# 10% backward -> 30cm
# 50% forward  -> 80cm
# 15% right    -> 60cm
# 25% left     -> 40cm

n = 20

b_f_r_l = [0.1, 0.5, 0.15, 0.25]
cumulative = []

for i in range(len(b_f_r_l)):
    if i == 0:
        cumulative.append(b_f_r_l[i] * 100)
    else:
        cumulative.append(cumulative[i - 1] + b_f_r_l[i] * 100)

print(cumulative)

dx = []
dy = []
direction = []
x = 0
y = 0
for i in range(n + 1):
    rd = np.random.randint(0, 99)
    if rd >= 1 and rd <= cumulative[0]:
        dx.append(x)
        y -= 30
        dy.append(y)
        direction.append('B')

    elif rd > cumulative[0] and rd <= cumulative[1]:
        y += 80
        dx.append(x)
        dy.append(y)
        direction.append('F')

    elif rd > cumulative[1] and rd <= cumulative[2]:
        x += 60
        dx.append(x)
        dy.append(y)
        direction.append('R')

    elif (rd > cumulative[2] and rd < cumulative[3]) or (rd == 0):
        x -= 40
        dx.append(x)
        dy.append(y)
        direction.append('L')

print(direction)
plt.plot(dx, dy)
plt.show()
