class Test:
    def __init__(self, value):
        self.value = value

#hasattr выдаст False
print(hasattr(Test, 'value'))

#После того как мы создали экземпляр класса, выдаст True
a = Test('value')
print(hasattr(a, 'value'))

#Поверить атрибут, если не найдено то возвращает null
print(getattr(Test, 'value', 'null'))