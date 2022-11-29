class User:
    def __init__(self, value):
        self.value = value
        self.arrage = [1, 2, 3]

    def __pow__(self, power, modulo=None):
        #Возвращает степень
        return self.value ** power

    def __reversed__(self):
        #Переворачивает список
        self.arrage.reverse()
        return self.arrage

    def __truediv__(self, other):
        #Деление
        return int(self.value / other)

a = User(10)

print(pow(a, 2))
print(a ** 2)

print(reversed(a))
print(a.__reversed__())

print(a / 2)