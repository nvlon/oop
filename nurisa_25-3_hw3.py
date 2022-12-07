
consonant = 'bcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщBCDFGHJKLMNPQRSTVWXZБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
vowels = 'aeiouyаиоуыэяеюиAEIOUYАИОУЫЭЯЕЮИ'
while True:
    consonant_count = 0
    vowels_count = 0
    word = input('Введите слово:')
    if word.lower() == "exit":
        break
    for i in word:
        if i. isalpha():
            if i in consonant:
                consonant_count += 1
            elif i in vowels:
                vowels_count += 1
    pro = (vowels_count / len(word))  * 100
    pro1 = round(pro, 2)
    print('Ваше слово:', word)
    print('Количество букв:', str(len(word)))
    print('Согласных букв:' , consonant_count)
    print('Гласных букв:', vowels_count)
    print("Гласные:", pro1, '%', 'Согласные:', 100-pro1 ,'%' )