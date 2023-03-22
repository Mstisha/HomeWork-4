from random import randint
a = int(input("Введите количество цифр первого множесвтва: "))
b = int(input("Введите количество цифр второго множесвтва: "))
x = set()
y = set()
for i in range(a):
    x.add(randint(1, 10))
        
for i in range(b):
    y.add(randint(1, 10))
print(x)
print(y)
z = x.intersection(y)
print(z)