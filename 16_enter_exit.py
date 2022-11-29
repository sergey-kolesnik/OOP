#Контекстный менеджер
class User:
    def __init__(self):
        self.arrage = [1, 2, 3]

    def __enter__(self):
        print('__enter__')
        return self.arrage

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        del self.arrage

a = User()
with a as arr:
    #то что мы реалезовали в __enter__, попадает в arr
    print(arr[0])

#после того как мы вышли из контекстного менелдера, вызывается __exit__