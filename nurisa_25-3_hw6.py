def first_word(words="Hello World"):
    if type(words) == str:
        first_word = words.split()
        return first_word[0]
    elif type(words) != str:
        return False


print(first_word())



def average(*args):
    return (int(sum(args) / len(args)))

print(average(1,  4, 8, 50))


def check_password(password):
    if len(password) > 6 and not password.isdigit() and not password.isalpha():
        return True
    else:
        return False

print(check_password(input('Введите пароль:')))
