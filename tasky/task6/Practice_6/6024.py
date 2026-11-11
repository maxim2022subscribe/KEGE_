from turtle import *
screensize(10_000,10_000)
tracer(0)
m = 20
lt(90)
for i in range(4):
    fd(19*m)
    rt(90)
    fd(30*m)
    rt(90)
up()
fd(2*m)
rt(90)
fd(8*m)
lt(90)
down()
for i in range(4):
    fd(93*m)
    rt(90)
    fd(97*m)
    rt(90)

for x in range(8,31): #23
    for y in range(2,20): #18
        teleport(x*m,y*m)
        dot(3,"red")
print(22*17)

update()
done()