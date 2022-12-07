class Human:
    # атрибуты уровня класса (переменная находящаяся внутри класса)
    head = 1
    body = 1
    # функция конструктор (метод)
    def __int__(self , name , age):
        self.name = name
        self.age = age
    # метод
    def run(self):
        print(f'{self.name} is run')
    def __str__(self):
        return f'{self.name} {self.age} {self.head}'

hum=Human("nvlon", 18)
hum.name = "aida"
hum.foots=2
hum.run()
print(hum,hum.foots)

class Raketa:
    toplivo=True
    kabina=1
    korpus='ironMan'
    human=None
    def run(self,human):
        print(f'{human} is Fly')
Raketa.run(hum.name)