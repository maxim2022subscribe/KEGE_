from string import printable as alph
print(alph)
def convert(num,sys):
    res = ""
    while num:
        res += str(num%sys)
        num//= sys
    return res[::-1] if res else "0"
cnt_ = 0
for N in range(1_000_000):
    if len(convert(N,5))==4 and len(convert(N,3))==5 and convert(N,16)[-2:] == "13":
        cnt_ +=1
print(cnt_)