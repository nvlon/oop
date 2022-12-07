import random
print(' загаданное число равно, больше или меньше' )
attempts = []
hidden_number = []

start = 1
finish = 100
count = 0

while True:
    n = (start + finish)//2
    answer = input(f'Ваше число - {n}? Да, больше или меньше?').lower()
    if answer.lower() == 'да':
        attempts.append(n)
        hidden_number.append(n)
        count += 1
        print('я угадал с',count ,'попытки!' )
        with open('results.txt','w', encoding = 'UTF-8') as file:
            file.write(f'Number of attempts: {count}; \nList of attempts: {list}; \nThe correct number: {hidden_number}')

        break

    elif answer == 'больше':
        finish = n + 1
        count += 1
        attempts.append(n)
    elif answer == 'меньше':
        start = n - 1
        count += 1
        attempts.append(n)
    else:
        print('Вы ввели неправильное значение! Вводить только да больше или меньше!')
