def convert(num,sys):
    res = ""
    while num:
        res += str(num%sys)
        num//= sys
    return res[::-1] if res else "0"
ans = []
for N in range(1,10_000):
    nb = convert(N,3)
    if sum(map(int,nb))% 3 == 0:
        nb = nb + "212"
    else:
        nb = nb + convert(sum(map(int,nb))*2,3)
    R = int(nb,3)
    if N == 11:
        print(R)
    if R >490:
        ans.append(R)
print(min(ans))