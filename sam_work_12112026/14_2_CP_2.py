num = 729**8 -3 ** 18 + 85
cnt_0 = 0
while num:
    if num%9 == 0: cnt_0 += 1
    num//=9
print(cnt_0)