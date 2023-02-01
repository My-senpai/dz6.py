# кратно ли число 3

a = list(map(int,(input('Введите число ').split())))
res = list(filter(lambda num: (num % 3 == 0), a))

if res:
    print(f"число {res} кратно трем")
else:
    print('ne kratno')