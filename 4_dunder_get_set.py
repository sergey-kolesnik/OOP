class Data:
    def __init__(self):
        self.value = ''

    def __get__(self, instance, owner):
        print('Данные:')
        #получить данные
        return self.value

    def __set__(self, instance, value):
        print('Данные записанны')
        #записать  данные
        self.value = value

class User:
    name = Data()
    surname = Data()

test = User()
test.name = 'test'
print(test.name)