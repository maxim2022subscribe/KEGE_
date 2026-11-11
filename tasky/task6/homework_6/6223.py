from turtle import *
screensize(10_000,10_000)
tracer(0)
m = 10
lt(90)
for i in range(9):
    fd(17*m)
    lt(90)
    fd(8*m)
    lt(90)
    fd(17*m)
up()
lt(90)
fd(3*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(4):
    fd(97*m)
    rt(90)
    fd(132*m)
    rt(90)

for x in range(-5,1): #6
    for y in range(-17,-4): #13
        teleport(x*m,y*m)
        dot(3,"red")
print(5+5 + 12 +12)
# прав ответ - 34
update()
done()