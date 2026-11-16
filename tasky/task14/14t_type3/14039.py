def convert(num,sys):
    r = ""
    while num:
        r += str(num%sys)
        num//=sys
    return r[::-1] if r else "0"
ans = []
for x in range(1,2031):
    num = 9**150 + 9**30 - x
    cnt = 0
    while num:
        if num % 9 == 0: cnt += 1
        num //= 9
    if cnt == 122:
        ans.append(x)
print(min(ans))