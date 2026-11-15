from string import printable as p
def convert(num,sys):
    r = ""
    while num:
        r += str(p[num%sys])
        num//=sys
    return r[::-1] if r else "0"
ans = []
for x in range(0,100):
    num = 3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 1*7**(2*x)
    nn = sum(map(int,convert(num,7)))
    if nn == 18:
        ans.append(x)
print(min(ans))
