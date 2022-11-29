class User:
    args = {
        'version': '1',
        'flag': '2'
    }
    def __init__(self):
        self.__dict__ = self.args

a = User()
b = User()

#Если мы изменим что то внутри класса, то это изменится во всех экземплярах