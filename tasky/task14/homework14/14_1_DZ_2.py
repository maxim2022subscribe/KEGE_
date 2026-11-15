num = 51*7**12 - 7**3 - 22
def convert(num,sys):
    res = ""
    while num:
        res += str(num%sys)
        num//= sys
    return res[::-1] if res else "0"
cnt_0 = 0
print(convert(num,7))
print(sum(map(int,convert(num,7))))