class User:
    version = 1

    def __init__(self, name='test'):
        self.name = name

    @classmethod
    def set_name(cls, value):
        cls.version = value


a = User()

b = User()

c = User()

#Изменили версию во всех экземлярах,
# так как метод класса используется для всего класса
a.set_name(3)

print(a.version)
print(b.version)

#Но если изменить версию в самом экземпляре, а не вов всем классе,
# то изсенения коснуться только экземпляра
c.version = 6
print(a.version)
print(c.version)

