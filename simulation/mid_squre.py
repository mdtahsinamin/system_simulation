n = 40
seed = 8537

pre = int(len(str(seed))/2)

rnd = []
for i in range(n):

    y = seed * seed
    square = str(y)
    length = int(len(square)/2)

    mid_square = square[length - pre: pre + length]
    rnd.append(mid_square)

    seed = int(mid_square)

print(rnd)