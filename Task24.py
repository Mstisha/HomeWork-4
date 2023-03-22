from random import randint

bush = int(input("Введите количество кустов: "))
x = []
for i in range(bush):
    x.append(randint(1, 10))
print(x)
count = sum(x[0:3])
max = 0
for i in range(len(x)):
    if count > max:
        max = count
    else:
        count = sum(x[i:i+3])
print(max)