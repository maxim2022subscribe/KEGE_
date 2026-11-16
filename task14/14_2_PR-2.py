from string import printable as p
ans = []
for x in p[10:14]:
    for y in p[9:int(x,36)]:
        num_1 = int(f"7{x}37{y}",14)
        num_2 = int(f"9{y}63",int(x,36))
        num_3 = int("15148",int(y,36))
        num = num_1 + num_2 - num_3
        ans.append([num,num // (int(x,36)+int(y,36))])
print(max(ans))






####################################

for x in range(10,14):
    for y in range(9,x):
        num_1 = int(f"7{p[x]}37{p[y]}",14)
        num_2 = int(f"9{p[y]}63",x)
        num_3 = int("15148",y)
        num = num_1 + num_2 - num_3