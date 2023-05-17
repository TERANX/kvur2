# Проект kvur2
# Система для решения квадратных уравнений

## Для чего нужна система.
* Решение квадратных уравнений
* Решение биквадратных уравнений
## Для кого эта система
* Студенты
* Школьники 
  * Начальная школа
  * Средняя школа
* * *
## Примеры использования

Для того чтобы запустить приложение выполните ` python3 kvtest.py` и введите нужные данные.



## Как происходит получение данных от пользователя

``` python
from math import sqrt
baddata = True
while baddata :
    try:
         a = int(input('Введите a: '))
         b = int(input('Введите b: '))
         c = int(input('Введите c: '))
         baddata = False
    except ValueError:
        print('Не удалось получить данные!!!')
        
```

| Название приложения | Польза приложения |
|---------------------|-------------------|
| kvtest.py           | Высокая           |

![Картинка123](https://cdn.eduonix.com/assets/images/header_img/2021030405504812780.jpg)
Для более успешного использования [мой сайт](https://www.nadejnei.net/)

## Молодец ли я?
-[x] молодец
-[ ] не молодец

*Курсив*

__Жирный__