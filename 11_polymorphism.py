#Полиморфизм в питоне, не похож на другие языки


#Реализовать полиморфизм в пайтон,
# класс принимает разные типы данных
# и выдает разный результат
from functools import singledispatch
class User:
    @singledispatch
    def get_value(value):
        print('default:', value)

    @get_value.register(int)
    def _(value):
        print('int:', value)

    @get_value.register(str)
    def _(value):
        print('str', value)

User.get_value([1, 2, 3])
User.get_value(1)
User.get_value('hello')