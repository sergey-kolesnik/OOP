class User:
    def __init__(self, value):
        self.value = value

    def __call__(self, comment):
        #этот метод поволяет вызывать экземпляр класса как функцию
        print('__call__', self.value)
        print('comment', comment)

a = User(10)
#Вызвали как функцию
a('test')
####################################################
class Test:
    #Позволяет создать итератор
    def __iter__(self):
        print('__iter__')
        self.arrage = [1, 2, 3]
        return self

    def __next__(self):
        if self.arrage:
            return f'__next__: {self.arrage.pop()}'
        else:
            raise StopIteration('self.arrage - закончился')

b = Test()

for check in b:
    print(check)