#списки, кортежи
#списки это неизменяемый тип данных ,который хранит какой- либо обьект
#списки создаются в квадратных скобках []
#list - список

# new = list(range(1,4))
# print(new)
# objects = (3,)
# new = tuple(new)
# print(new)
#
# print(objects)
# print(type(objects))




# objects = [1, 1, 1, 2, 2, 2, 2 ]
# new = objects.copy()
# new [-1] = 5
# print(objects == new) - проверка на схожесть
# print(objects is new) - проверка на идентичность
# print(objects)
# print(new)
# print(id(objects))
# print(id(new))



# new = list(range(1,4))
#
# objects = [1, 1, 1, 2, 2, 2, 2 ]
#
# max_ap = 1
# for i in objects:
#     if objects.count(i)> max_ap:
#         max_ap = objects.count(i)
#         print('max', max_ap)
# print(i if objects.count(i) == max_ap else 0)
# print(objects.count(5))
# objects.sort()
#objects.sort(reverse=True) (- меняет список)
# print(min(objects))
# print(max(objects))

"""удаление"""
# objects = [i for i in objects if type (i) != str]
# del objects[4:7]
# objects.remove(True) #- по значению удаляет
# objects.remove(4.7)
# objects.pop(0) #- по индексу
# deleted = objects.pop(0)
# print(deleted)

"""изменение"""
# objects[0], objects[3]= objects[3], objects[0]
# objects[objects.index(False)] = 'Bishkek'
# objects[0] = objects[0].upper()
# objects[0] = objects[0].title()
# objects[2] += 15
# del objects[-1][1]

"""добавление"""
# objects.append('bishkek')
# objects.insert(3, 100) (insert - вставляет в опред. место)
# objects.append(new)
# objects.extend(new) (extend - расширение списка)
# objects += new


# print(objects)
# print(type(object))
