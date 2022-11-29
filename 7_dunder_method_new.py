class Test:
    #Используем не .self а cls
    def __new__(cls, *args, **kwargs):
        print('Создаем экземпляр класса!')
        instance = super().__new__(cls)
        #старая версия
        # instance = super(Test, cls).__new__(cls)
        return instance

    def __init__(self, name):
        print('создание экземпляра')
        self.name = name


