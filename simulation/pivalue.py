import math
import random
import numpy as np
import matplotlib.pyplot as plt

n = 500001
m = 0

dx=[]
dy=[]

for i in  range(n):
    x = random.random()
    y = random.random()
    dx.append(x)
    dy.append(y)
    if x**2 + y**2 <=1:
        m+=1

pi = (m/n)*4

print(pi)
