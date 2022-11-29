class Test:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        #для перегрузки оператора сложения
        return self.value + other

    def __sub__(self, other):
        #для перегрузки оператора вычитания
        return self.value - other

    def __eq__(self, other):
        #Для перегрузки оператора сравнения
        if other == self.value:
            return True
        else:
            return False

    def __hash__(self):
        #Для хеширования
        return hash(self.value)


# тем самым мы можем задавать новое поведение
a = Test(10)
print(a + 1)
print(a - 1)
print(a == 1)
print(hash(a))