import random
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def func(x):
    return x**4/3

lower_bound = 1
upper_bound = 5

x = sp.Symbol("x")
exact_integration = sp.integrate(func(x), (x, lower_bound, upper_bound))

dx =[]
dy = []

n = 50000
m = 0
exact_integration+=2

for i in range(n):
    dx.append(random.randint(10, 50)/10)
    dy.append(np.random.rand() * exact_integration)

    if dy[i] <= func(dx[i]):
        m+=1


I = (m/n)*(exact_integration * (upper_bound - lower_bound))
print(I)

x = []
y = []

for i in range(12):
    x.append(i)
    y.append(func(x[i]))

plt.scatter(dx, dy)
plt.plot(x, y)
plt.show()



