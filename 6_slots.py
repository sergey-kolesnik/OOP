class User:
    #Атрибут __slots__
    #Добавляет новый слой безопастности, пользователь не сможет создать новые атрибуты
    __slots__ = ['name', 'age']
    def __init__(self, name='name1', age=20):
        self.name = name
        self.age = age

a = User()
#Если создать атрибут, то будет ошибка, так как он не указан в __slots__
a.test = 1