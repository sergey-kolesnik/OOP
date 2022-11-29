class User():
    #Указываем значение по умолчанию
    def __init__(self, name='test'):
        #Мы не контролируем запись и чтение атрибута, это совсем не безопасно,
        # одно нижнее подчеркивание делает наш атрибут приватным, его не нужно трогать или как то изменять
        self._name = name

    @property
    def name(self):
        #геттер для того что бы вернуть значение атрибута
        print('вернули значение атрибута')
        return self._name

    @name.setter
    def name(self, value):
        #геттре для того что бы задать значение атрибуту
        print('атрибут изменен')
        self._name = value

    @name.deleter
    #удалить атрибут
    def name(self):
        print('атрибут удален')
        del self._name

a = User()
#задать имя:
a.name = 'test'
#вывести имя:
print(a.name)
#удалить атрибут:
del a.name


