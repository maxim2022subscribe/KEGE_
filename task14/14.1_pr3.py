def convert(num,sys):
    res = ""
    while num:
        res += str(num%sys)
        num//= sys
    return res[::-1] if res else "0"


num = 5*216**3031 + 4*36**3042 -3*6**3053 - 3064

print(sum(map(lambda x: int(x,6),convert(num,6))))