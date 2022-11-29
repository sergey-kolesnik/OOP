class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print('in counter:')

    def test(self):
        print('test')

#обернули в декоратор
@Counter
def printer():
    print('printer')

#при вызове функции, она проходит через класс и ей доступны все аргументы и методы
printer()
printer.test()
printer()
printer()
printer()
print(printer.count)