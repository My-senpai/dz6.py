#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


number = 0
a = input('Введи вещественное число ')
a = a.replace('.', '')
for index, num in enumerate(a):
    number+=int(num)
print(f'ответ будет = {number}')