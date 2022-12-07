# работа с файлами txt
# w - write
# a - add
# r - read
# x - safety method

# 4, 52, 70, 60, 58, 55, 53, 54
# 50, 75, 87, 93, 90


data = {}

with open('test.txt', 'r') as file:
    for i in file.readlines():
        data[i.split()[0]] = i.split()[-1]

print(
    f"кол-во: {len(data)}\n"
    f"правильно: {list(data.values()).count('правильно')}\n"
    f"неправильно: {list(data.values()).count('неправильно')}\n"
    f"список имен: {set(data.keys())}"
)



# from random import randint, choice
#
# students = [8, 16, 10, 13, 14, 7, 6, 15, 4, 18, 12, 1]
#
# while len(students) != 0:
#     print(students)
#     first, second = randint(1, 12), randint(12, 99)
#     right = first * second
#     student_id = choice(students)
#     name = input(f"имя студента {student_id}: ").title()
#     try:
#         user_answer = int(input(f"сколько будет {first} * {second} {name} ?"))
#     except:
#         print('только целые числа!')
#         continue
#     if user_answer == right:
#         print('alright!')
#         with open('test.txt', 'a') as file:
#             file.write(
#                 f"{name}: {first} * {second} = {user_answer} ({right})"
#                 f" правильно\n"
#             )
#     else:
#         print(f'no! {right}')
#         with open('test.txt', 'a') as file:
#             file.write(
#                 f"{name}: {first} * {second} = {user_answer} ({right})"
#                 f" неправильно\n"
#             )
#     students.remove(student_id)



# while True:
#     filename = input('имя файла: ')
#     if filename == 'exit':
#         break
#     with open(f'{filename}.txt', 'w') as file:
#         file.write(input('что запишем? \n'))

# new = open('file.txt', 'w', encoding='UTF-8')
# new.write('Бишкек, Кыргызстан')
# new.close()

# with open('new.txt', 'w') as file:
#     file.write('KGZaaaa')

# with open('new.txt', 'a') as file:
#     file.write('\n22222222')

# with open('text.txt', 'x') as file:
#     file.write('sdfsdfsdfewrgrt')

# from time import sleep as укта
#
# with open('new.txt', 'r') as file:
#     for letter in file.readlines():
#         укта(1)
#         print(letter, end='')

    # print(file.readlines()[0].split()[0])
    # print(type(file.readline()))
    # print(file.readlines()[-2])
