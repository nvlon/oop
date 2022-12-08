# парадигмы ооп
class Robot:
    brain = True

    def __init__(self, name, model, color, destination):
        self.name = name
        self.model = model
        self.color = color
        self.destination = destination



    def __str__(self):
        return f'name is {self.name}\n' \
               f'model is {self.model}\n' \
               f'color is {self.color}\n'\

    def desti (self):
        print(self.dest)


robot = Robot('Влад', 'a4', 'blue', 'снимать видео')
print(robot)
print(robot.desti())
#3 парадигмы ооп
#1-наследование
#2-полиморфизм
#3-инкапсуляция
#super - унаследует класс

# дочерний класс
class Robot2(Robot):
    brain=True
    def __init__(self, name, model, color, destination,fly):
        super().__init__(name, model, color, destination)
        Robot.__init__(self, name, model, color, destination)
        self.fly=fly
    def desti(self):
        self.fly=False
        print(self.fly)


robot2=Robot2('termonator', 'T1001', 'pink', 'отбирает одежду',True)
print(robot2.fly)
robot2.desti()
print(robot2.fly)
print(robot2.brain, robot.brain)

class Robot3(Robot2):...

MegaTron=Robot3('TRANSformer', 'Desipticon', 'RED','WARS', True)
MegaTron.desti()

class Human: