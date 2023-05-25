import numpy as np
def mid_square_random(n):
    seed = 8537

    pre = int(len(str(seed)) / 2)

    rnd = []
    for i in range(n):
        y = seed * seed
        square = str(y)
        length = int(len(square) / 2)

        mid_square = square[length - pre: pre + length]
        rnd.append(int(mid_square)/10000)

        seed = int(mid_square)

    return rnd


def kolmogorov(rand, n):
    random_sort = np.sort(rand)

    ibyN = []

    for i in range(n):
        ibyN.append(i/n)

    positive_deviation = []
    negative_deviation = []

    for i in range(n):
        if ibyN[i] - random_sort[i] < 0:
            continue
        else:
            positive_deviation.append(ibyN[i] - random_sort[i])

    for j in range(n):
        if j == 0:
            negative_deviation.append(random_sort[j])

        elif random_sort[j] - ibyN[j - 1] < 0:
            continue

        else:
            negative_deviation.append(random_sort[j] - ibyN[j - 1])


    max_d = max(positive_deviation)
    min_d = max(negative_deviation)
    largest = max(max_d, min_d)

    alpha = 0.05
    critical_value = 0.294
    another_value = 0.356

    if largest < critical_value:
        print("95% Uniformity")

    elif largest < another_value:
        print("99% Uniformity")
    else:
        print("NO")



n = 20
radn = mid_square_random(n)

kolmogorov(radn, n)