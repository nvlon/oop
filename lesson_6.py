# Функции, аргументы: *args, **kwargs.
# DRY - don't repeat yourself
# def - definition

""" Доп задание.
написать свои варианты функций sum(), max(), min()"""
# print(sum([1, 2, 3]))
# print(max([1, 2, 3]))
# print(min([1, 2, 3]))




from random import choice

students = [16, 3, 12, 8, 19, 13, 6, 14, 7, 15, 4, 21, 1]
materials = [1, 2, 3, 4, 5, 6]

answers = {}

while len(students) != 0:
    print(students)
    student_id = choice(students)
    name = input(f'имя студента под номером {student_id}: ')
    rate = int(input(f'{name} отвечает на вопрос из темы {choice(materials)}'))
    answers[name] = rate
    students.remove(student_id)

for name, rate in answers.items():
    print(f'{name}: {rate}')


# def days(**kwargs):
#     return sum(kwargs.values())
#
# print(days(monday=1, tuesday=2))

# def plus(a, *args, b=0):
#     print(f'a: {a}, b: {b}, args: {args}')
#     return sum(args) / a
# print(plus(2, 4, 6, 8, 56))




# def наименование(параметры):
#     тело функции
#     возврат значения
# наименование(аргументы)

# def len1(sequence: str or list) -> int:
#     """Принимает последовательность, вщзвращает кол-во элементов
#     в указанной последовательности.
#     """
#     counter = 0
#     for _ in sequence:
#         counter += 1
#     return counter
# print(len1([1, 4, 6, 7]))
# print(len1.__doc__)

# num = len('python')
# print(num + num)
# print(len('python'))

# def greet(name='name', surname='surname'):  # name - обязательный позиционный параметр
#     print(f'name: {name.title()}, surname: {surname.title()}')
#
# greet('azamat', 'alimov')  # azamat - обязательный позиционный аргумент
# greet(surname='kalykova', name='alina')  # keyword arguments (именованные аргументы)
# greet()

# def get_square(width, length):
#     return width * length
#
# square_2 = get_square(width=int(input('ширина: ')), length=int(input('длина: ')))
# square_hall = get_square(8, 15)

# width = 5
# length = 7
# square_2 = width * length
# print(square_2)
#
# width = 8
# length = 15
# square_hall = width * length
# print(square_hall)
