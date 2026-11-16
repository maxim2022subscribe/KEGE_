from string import printable as p
def convert(num,sys):
    res = ""
    while num:
        res += p[num%sys]
        num//= sys
    return res[::-1] if res else "0"

num = 283**382 + 9**15 + 2**3

nb = convert(num,14)
BB = nb.count("b")
CC = nb.count("c")
print(abs(BB-CC))