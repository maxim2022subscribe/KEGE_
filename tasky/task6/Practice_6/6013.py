from turtle import *
screensize(10_000,10_000)
tracer(0)
m = 20
lt(90)
rt(90)

for i in range(3):
    rt(45)
    fd(10*m)
    rt(45)
rt(315)
fd(10*m)
for i in range(2):
    rt(90)
    fd(10*m)

for x in range(-50,50): #23
    for y in range(-50,50): #18
        teleport(x*m,y*m)
        dot(3,"red")
print(13*13 + 7)
#13*13 + 7
update()
done()