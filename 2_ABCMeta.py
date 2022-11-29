from abc import  ABCMeta, abstractmethod

#Создали абстрактный класс
class User(metaclass=ABCMeta):
    @abstractmethod
    def go_to(self):
        pass

#наследовали от него
class Test(User):
    #переопределили метод
    def go_to(self):
        print('go')