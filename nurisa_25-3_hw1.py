biskek = float(input('Введите температуру Бишкека :'))
yssyk_ul = float(input('Введите температуру Ыссык-Куля :'))
batken = float(input('Введите температуру Баткена :'))
osh = float(input('Введите температуру Оша :'))
jalal_abad= float(input('Введите температуру Джалал-Абада :'))
naryn = float(input('Введите температуру Нарына :'))
talas = float(input('Введите температуру Таласа :'))
avarage = round((biskek + yssyk_ul + batken + osh + jalal_abad + naryn + talas) / 7 , 1)
print(f'Средний показатель температуры воздуха по КР на сегодня{avarage} °C ')
