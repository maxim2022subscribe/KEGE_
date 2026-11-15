from string import printable as p
def convert(num,sys):
    res = ""
    while num:
        res += str(p[num%sys])
        num//= sys
    return res[::-1] if res else "0"
for N in range(3,36):
    if convert(41,N)[-1] == "2" and convert(131,N)[-1] == "1":
        print(N)
        break