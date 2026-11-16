from math import ceil,log2
for V in range(1,10_000):
    L = 110
    N = 1030
    i = ceil(log2(N))
    I = ceil(L*i/8)
    mm = I * 32_768
    if V >= ceil(mm/1024):
        print(V)
        break