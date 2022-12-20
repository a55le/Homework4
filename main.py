#Задание 1
a = input('Введите элементы списка через пробел')
b = a.split(' ')
с = 0
for i in range(len(b)):
    if i % 2 != 0:
        с = с + int(b[i])
print(с)
#Задание 2
a = input('Введите элементы списка через пробел')
a2 = a.split()
if len(a2) % 2 != 0:
    range2 = int(len(a2) / 2) + 1
else:
    range2 = int(len(a2) / 2)
b = [0] * range2
len1 = 0
len2 = -1
for i in range(range2):
    b[i] = int(a2[len1]) * int(a2[len2])
    len1 = len1 + 1
    len2 = len2 - 1
print(b)_2 = index_2 + 1
print(c)
#Задание 3
a = [1.1, 1.2, 3.1, 5, 10.01]
b = []
for i in range(len(a)):
    b.append(a[i] - int(a[i]))
difference = max(b) - min(b)
print(difference)
#Задание 4
a = int(input('Введите число в десятичной системе'))
c = ''
while a != 1:
    b = a % 2
    c = c + str(b)
    a = a // 2
if a == 1:
    d = c + '1'
else:
    d = c
e = d[::-1]
print(e)
#Задание 5
number_fibonachi = int(input('Введите число'))
fibonachi = []
middle = [0]
plus_fibonachi = [None] * (number_fibonachi + 1)
minus_fibonachi = [None] * number_fibonachi
plus_fibonachi[0] = 0
plus_fibonachi[1] = 1
minus_fibonachi[7] = 1
i2 = number_fibonachi - 1
for i in range(i2):
    plus_fibonachi[i + 2] = plus_fibonachi[i] + plus_fibonachi[i+1]
plus_fibonachi.pop(0)
i3 = -1
for i in range(i2):
    minus_fibonachi[i] = -plus_fibonachi[i3]
    i3 = i3 - 1
fibonachi = minus_fibonachi + middle + plus_fibonachi
print(fibonachi)