from math import ceil,log2
N = 8192
i = ceil(log2(N))
WH = 1024*960
M = i*WH * 160
v = 14_680_064
t = M/v

print(t)