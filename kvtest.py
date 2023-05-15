import math
baddata = True
while baddata == True:
    try:
         a = int(input('Введите a: '))
         b = int(input('Введите b: '))
         c = int(input('Введите c: '))
         baddata = False
    except:
        print('Не удалось получить данные!')

D = (b * b) - (4 * a * c)

if D > 0:
    d = math.sqrt(D)
    x1 = ((-b) + d) / (2 * a)
    x2 = ((-b) - d) / (2 * a)
    printf(f'Уравнение имеет два корня x1 = {x1}, x2 = {x2}.')
elif D == 0:
    x1 = (-b) / (2 * a)
    printf(f'Уравнение имеет один корень x1 = {x1}.')
else:
    print('Уравнение не имеет корней')