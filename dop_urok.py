#горячие клавиши
# cntl + d = копировать вставить
# command + c command + v
# command + d
# command + z
# cntl + a = выделяет весь текст
# command + a

# cntl + shift + Up/down = сдвиг строки (вверх ,вниз)
# command + shift + Up/down
# cntl + / = commend / no commend

# cntl + x = копирует / вырезает
# command + x

# cntl + alt + l = выравнивает код
# command + alt +l

# alt + курсор = ввод по тем местам,  где вам нужно

# cntl + tab = переход по страничкам
# cntl + tab + shift  = переход по страничкам  в обратную сторону

# cntl + tab = переход по приложениям
# cntl + shift + tab  = переход по приложениям в обратную сторону

# cntl + t = новое окошко в гугле
# cntl + n = новое приложение  гугла
# alt + f4 = выходит с приложения
# \n - переход на след. строку



#hw1
biskek = float(input('Введите температуру Бишкека :'))
yssyk_ul = float(input('Введите температуру Ыссык-Куля :'))
batken = float(input('Введите температуру Баткена :'))
osh = float(input('Введите температуру Оша :'))
jalal_abad= float(input('Введите температуру Джалал-Абада :'))
naryn = float(input('Введите температуру Нарына :'))
talas = float(input('Введите температуру Таласа :'))
avarage = round((biskek + yssyk_ul + batken + osh + jalal_abad + naryn + talas) / 7 , 1)
print(f'Средний показатель температуры воздуха по КР на сегодня{avarage} °C ')

#hw2
day = int(input('Введите день рождения: '))
month = int(input('Введите месяц рождения: '))

if (day >= 21 and day <= 31 and month == 3 ) or (day >= 31 and day <= 20  and month == 4):
  print('овен')

elif (day >= 21 and day <= 31 and month == 4 ) or (day >= 1 and day <= 21  and month == 5):
  print('телец')

elif (day >= 22 and day <= 31 and month == 5 ) or (day >= 1 and day <= 21  and month == 6):
  print('близнецы')

elif (day >= 22 and day <= 31 and month == 6 ) or (day >= 1 and day <= 22  and month == 7):
  print('рак')

elif (day >= 23 and day <= 31 and month == 7 ) or (day >= 1 and day <= 21  and month == 8):
  print('лев')

elif (day >= 22 and day <= 31 and month == 8 ) or (day >= 1 and day <= 23  and month == 9):
  print('дева')

elif (day >= 24 and day <= 31 and month == 9 ) or (day >= 1 and day <= 23  and month == 10):
  print('весы')

elif (day >= 24 and day <= 31 and month == 10 ) or (day >= 1 and day <= 22  and month == 11):
  print('корпион')

elif (day >= 23 and day <= 31 and month == 11 ) or (day >= 1 and day <= 22  and month == 12):
  print('стрелец')

elif (day >= 23 and day <= 31 and month == 12 ) or (day >= 1 and day <= 20  and month == 1):
  print('козерог')

elif (day >= 21 and day <= 31 and month == 1) or (day >= 1 and day <= 19 and month == 2):
  print('водолей')

elif (day >= 20 and day <= 31 and month == 2 ) or (day >= 1 and day <= 20  and month == 3):
  print('рыбы')

else:
    print('вы уверены, что написали правильно?')






