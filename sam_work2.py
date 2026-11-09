#создать список с квадратами чисел от 1 до 9 вкл
data = "12796826871684684"
kvadr = [i**2 for i in range(1,10) if i%2 == 0]
print(kvadr)