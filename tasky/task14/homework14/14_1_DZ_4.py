from string import printable as p
def convert(num,sys):
    r = ""
    while num:
        r += str(p[num%sys])
        num//=sys
    return r[::-1] if r else "0"
num = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
print(num)
print(convert(num,16))
print(sum(map(lambda x: int(x,10) if p.index(x)<=10 else 0,convert(num,16))))

