def TurnTo(n,sys):
    r = ""
    if n!=0:
        while n:
            r += str(n%sys)
            n //= sys
        return r[::-1]
    else:
        return "0"
ans = []

for N in range(100):
    nb = TurnTo(N,4)
    if (nb.count("1")+nb.count("2")*2+nb.count("3")*3)%2==0:
        nb = nb + nb[-2:]
    else:
        nb = "2"+ nb +"0"
    R = int(nb,4)
    if R > 120 and R%2==0:
        ans.append(R)
print(min(ans))