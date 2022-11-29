class Test:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        #Умножить атрибут на значение
        return self.value * other



a = Test(10)
print(a * 3)

class User:
    def __init__(self, arrage=[1, 2, 3]):
        self.arrage = arrage
    #Может извлечить элемент из списка по индексу
    def __getitem__(self, item):
        return self.arrage[item]

    #Можем записать в список элемент
    def __setitem__(self, key, value):
        self.arrage[key] = value

    #Удалить элемент из списка
    def __delitem__(self, key):
        del self.arrage[key]
        print('Значение удалено')
#Извлекаем
a = User()
print(a[0])
a[2] = 10
print(a[2])
del a[1]