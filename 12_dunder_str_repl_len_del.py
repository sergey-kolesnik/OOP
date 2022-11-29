class User:
    def __init__(self, value='test'):
        self.value = value

    #Длина атрибута
    def __len__(self):
        return len(self.value)

    #Атрибут в строке
    def __str__(self):
        return self.value
    #Отладочная информация
    def __repr__(self):
        return f"{self.value} {id(self.value)}"

    def __del__(self):
        print('Экземпляр удален')

a = User()

print(str(a))
print(len(a))
print(repr(a))
del a