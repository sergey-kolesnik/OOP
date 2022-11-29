class User:
    #При создании экземпляра всегда вызывается __init__, может принимать аргументы, которые сразу же помещаем в .self
    #тоесть в некую оболочку самого экземпляра, если мы проходим черезе __init__,
    # наши новые переменные будут находится внутри экземпляра и при изменения глобально в классе,
    # другие экземпляры изменяться не будут
    def __init__(self,  *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
        #Мы можем вызывать метод из инита, главное указать .self
        self.get_name()

    def get_name(self):
        print(self.args)
        print(self.kwargs)

a = User( *[1, 2, 3], **{'test': 'test'})