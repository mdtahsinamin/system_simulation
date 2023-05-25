import numpy as np
import  matplotlib.pyplot as plt

length = 1000
width = 600

deviation_x = 500
deviation_y = 300

n = 50
hit = 0
step = 0
poin_x=[]
poin_y=[]
for i in range(n):
    x = np.random.randn() * deviation_x
    y = np.random.randn() * deviation_y

    poin_x.append(x)
    poin_y.append(y)

    if (x>= -deviation_x and x<= deviation_x) and ( y >= -deviation_y and y<= deviation_y) :
       hit+=1

    step+=1

mis = step - hit
print((hit/step) * 100)
print((mis/step) * 100)


area_x = [-500, 500, 500, -500, -500]
area_y = [-300, -300, 300, 300, -300]

plt.plot(area_x, area_y, color="red")
plt.scatter(poin_x, poin_y)
plt.show()
