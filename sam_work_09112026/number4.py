def TurnTT(num,sys):
    R = ""
    if not num:
        return "0"
    while num:
        R+=str(num%sys)
        num//=sys
    return R[::-1]
r = 0
min = 10**20
ans = []
for N in range(1,10_000):
    r = TurnTT(N,3)
    if N%2==0:
        r = r + r[-2:]
    else:
        r = r + TurnTT(sum(map(int,r)),3)
    r = int(r,3)
    if N>9:
        ans.append([r,N])
print(min(ans))
