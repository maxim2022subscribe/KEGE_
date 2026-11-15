from string import printable as p
print(p)
print(len(p))
for x in range(16,32):
    num1 = int("17496",x)
    num2 = int("91f83",x)
    num3 = int("d9543",x)
    num =num1+num2+num3
    if num%12==0:
        print(x,num//12)