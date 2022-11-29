#Наследование
#Волшебник Wizard
#Воин Fighter
#Паладин Paladin

class Base:
    def __init__(self, health):
        self.health = health
    #Базовый класс
    def go_to(self):
        print('go')

    def get_damage(self):
        self.health -= 10
        print('get_damage')

    def restore_health(self):
        self.health += 10
        print('restore_health')

#Дочерние классы наследуются от класса родителя Base
class Wizard(Base):
    def __init__(self,health=100):
        super().__init__(health)
    #Переопределили метод дочернего класса
    def get_damage(self):
        print("None")

class Fighter(Base):
    def __init__(self, health=200):
        super().__init__(health)

class Paladin(Base):
    pass

