def convert(num,sys):
    r = ""
    while num:
        r += str(num%sys)
        num//=sys
    return r[::-1] if r else "0"
ans = []
for x in range(1,3001):
    num = 3**100 - x
    cnt = 0
    while num:
        if num % 3 == 0: cnt += 1
        num //= 3
    if cnt == 1:
        ans.append(x)
print(max(ans))