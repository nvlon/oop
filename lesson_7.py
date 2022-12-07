# лямбда исключения
# lambda arguments: expression
# лямбда это  укороченный вид функции
# try:
#     code
# except:
#     message
# try:
#     print(10/0)
# except:
#     print('на ноль делить нельзя!')
#
# if ZeroDivisionError:
#     print('на ноль делить нельзя!')
# else:
#     print(10/0)

# season = 'autumn'
# while True:
#     user = input('Введите сезон :')
#     if user != season :
#         raise Exception('неправильный сезон')
#     else:
#         print('ok')

def first_word(sentence = 'hello world'):
    if type (sentence) != str:
        return False
    return sentence.split()[0]
    return first_word('python bishkek') == False, 'неправильно'
print(first_word('python bishkek'))





# word = 'python'
# while True:
#     try:
#      user_input = int(input('Введите индекс:'))
#      print(word[user_input])
#     except:
#         print('неправильный индекс, Вводить только числа')
#     except IndexError:
#         print('неправильный индекс')
#     except ValueError:
#         print('Вводить только числа!')
#     except SyntaxError:
#         print('что-то не так!')


# current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
# sorted_list = lambda x: (sorted(i) for i in x)
# print(sorted_list)
#
# second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
# result = second_largest(current_list, sorted_list)
# print(result)

# new = [sorted(i) for i in current_list]
# print(new)
#  for i in new :
#      print(i[len (i) - 2])

# numbers = list(range(1 , 10 +1))
# print(numbers)
# filtered_numbers = list(filter(lambda x: x < 6 , numbers))
# filtered_numbers = [ i * 2 for i in numbers if i < 6]
# print(filtered_numbers)



# mapped_list = list (map(lambda x : x * 2 , numbers))
# mapped_list = [i*3 for i in numbers]
# print(mapped_list)


# a = lambda a, b: a+b
# print(a(2 , 3))
#
# def b (a , b):
#     return a + b
# print(b(3 , 2))


# def up_letter(word: str):
#     return word.title()
#
# def last_up (word: str) -> str:
#     return word [:-1 ] + word [-1].upper()
#
# def show_words (sequevce, func):
#     for word in sequevce:
#         print(func(word))
#
# show_words(['python', 'bishkek' , 'geektech'], last_up)
# show_words(['python', 'bishkek' , 'geektech'], lambda word:word [:-1 ] + word [-1].upper() )
