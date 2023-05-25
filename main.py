import random
import numpy as np
import matplotlib.pyplot as plot


def func_integr(x):
    return x ** 3


lower_bound = 2
upper_bound = 5

dx = []
dy = []
n = 0
m = 0

iteration = 50000
for i in range(iteration):
    dx.append(random.randint(20, 50) / 10)
    dy.append(np.random.rand() * 140) # 0 - 1 * 140

    if dy[i] <= func_integr(dx[i]): # y<= x^3
        m += 1

    n += 1

I = (m / n) * (140 * (upper_bound - lower_bound))
print(I)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
y = []
for i in range(len(x)):
    y.append(func_integr(x[i]))

plot.scatter(dx, dy)
plot.plot(x, y)
plot.show()
