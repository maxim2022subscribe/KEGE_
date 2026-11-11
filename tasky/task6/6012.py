from turtle import *
screensize(10_000,10_000)
tracer(0)
m = 10
for i in range(2):
    fd(13*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
fd(8*m)
rt(90)
bk(3*m)
lt(90)
down()
for i in range(2):
    fd(16*m)
    rt(90)
    fd(8*m)
    rt(90)
for x in range(8,14): # вкл точки на пересеч линиях
    for y in range(-5,1): # вкл точки на пересеч линиях
        teleport(x*m,y*m)
        dot(3,"red")
print(14*21 + 17*9 - (6*6))
update()
done()