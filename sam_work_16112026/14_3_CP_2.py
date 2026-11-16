from math import log2,ceil

for N in range(1,10_000):
    L = 2783
    i = ceil(log2(N))
    I = ceil(L*i/8)
    M = I*3_845_627
    if M >= 11*1024*1024*1024:
        print(N)
        break