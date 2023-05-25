rnd = [25]

a = 13
b = 9
m = 63
j = 1
for i in range(50):
    rnd.append( (a * rnd[j - 1] + b) %m)
    j+=1

print(rnd)