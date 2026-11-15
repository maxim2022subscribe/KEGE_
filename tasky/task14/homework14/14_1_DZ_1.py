num = 16**820 - 2**761 + 14
def convert(num,sys):
    res = ""
    while num:
        res += str(num%sys)
        num//= sys
    return res[::-1] if res else "0"
cnt_0 = 0
print(convert(num,4))
