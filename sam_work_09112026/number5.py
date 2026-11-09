ans = []
for N in range(1,10_000):
    nb = bin(N)
    if N%8==0:
        nb = nb + nb[-2]
    else:
        nb = nb + bin((N%8)*2)
    R = int(nb[2:],2)
    if R > 3000:
        ans.append([R,N])
print(min(ans))