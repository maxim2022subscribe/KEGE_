from string import printable as p
def intp(num,sys):
    s = 0
    for l in range(0,len(num)):
        s += p.index(num[len(num)-1-l]) * sys**l
    return s
nn = 0
for x in p[10:67]:
    for y in p[:p.index(x)]:
        num1 = intp(f"73{x}1{y}",67)
        num2 = intp(f"49{y}6",p.index(x))
        num = num1+num2
        nn+=1
        print(num,x,y)
print(nn)