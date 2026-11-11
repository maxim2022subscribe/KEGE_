from turtle import *
screensize(10_000,10_000)
#tracer(0)
m = 20
for i in range(3):
    fd(3*m)
    rt(90)
    fd(4*m)
    lt(90)
rt(180)
fd(9*m)
rt(90)
fd(12*m)
up()
bk(2*m)
lt(90)
down()
for i in range(3):
    fd(2*m)
    lt(90)
    fd(3*m)
    rt(90)
lt(180)
fd(8*m)
lt(90)
fd(9*m)
lt(90)
fd(2*m)

for x in range(0,3): # 3
    for y in range(-11,-1): #10
        teleport(x*m,y*m)
        dot(3,"red")
print(126-18)
# прав ответ - 108
update()
done()