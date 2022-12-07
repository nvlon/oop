# циклы : for , while
# item , iterable
# цикл for предназначен для перебора эдементов структур данных и некоторых других обьектов.




# cash = 100
# percents = 0.1
# years = 5
#
# counter = 1
# for year in range(1, years+1):
#     cash =  round(cash * percents + cash, 1)
#     print (f'year : - {counter} - {cash}')
#     counter += 1

#range - диапозон чисел
# for i in range (1, 4):
#     for k in range (1,4):
     # print(i, k)


# word = 'аксессуар'
#
# for letter in word :
#     if letter == 'у':
#         print("мы пропускаем 'c' ")
#         continue - продолжить с пропуском оставшей части кода
#         print(letter)


    # if letter == 'e':
    #     print ('цикл завершен!')
    #     break - оператор завершение цикла
    # print(letter)
    # print(letter.upper(), end='')

# c = 0
# while c != 5:
#     if c == 3:
#         print('мы устали')
#         break
#     c += 1
#     print(c)
# print(number)
# while True:
#     print('hello' , c)
#     c += 1

# while c != 5:
#     if c == 3:
#         print('мы устали')
#         continue
#     c += 1
#     print(c)


# c = 0
#
# from time import sleep
# while True :
#     sleep(1)  - задержка в секунде
#     print('hello', c)
#     c += 1

# c = 0
# while True:
#     print('hello' , c)
#     c += 1
#     if c == 100:
#           break
#
# while True:
#     password = input('enter password:')
#     if password == 'exit':
#         break
#задание
# eng = "gwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
# user_input = input ('введите слово:')
# for i in user_input:
#     if i in eng:
#         print(rus[eng.index(i)], end='')
#     else:
#         print(eng[rus.index(i)], end='')
# print(rus[eng.index('r')])

