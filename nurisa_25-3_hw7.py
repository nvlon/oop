ten = list(range(1, 11))
evens = list(filter (lambda i : i % 2 == 0 , ten))
evens0 = list (map (lambda i : i ** 2 , evens))
print(evens0)


def function (list =(list (ten ))):
    while True:
        index = input ('Введите индекс для вывода обьекта из списка :')
        if index.lower() == 'exit' or index.lower() == 'Выход' or index.lower() == 'Exit' or index.lower() == 'выход' :
            break
        try:
            print(list[int(index)])
        except:
            print('Неверный индекс ,возможно данного индекса не существует!')

        function()