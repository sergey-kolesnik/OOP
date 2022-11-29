class User:
    name = 'test'
    age = 17


#Функция getattr(class, 'имя') можем указывать имя атрибута,
# в качестве строки и перебирать все эти значения в цикле,
# можно получать так же и функции getattr(User, "имя функции")()- вызвать
print(getattr(User, 'name'))
#Указав 3 аргумент, не будет ошибки
print(getattr(User, 'name', None))

#setattr - для добавления данных на лету,
a = User
setattr(a, 'surname', 'test_2')
print(getattr(a, 'surname'))

#Можно добавить атрибут в сам Класс:
setattr(User, 'surname', None)

#Можно удалить атрибут прям из класса:
delattr(User, 'name')

#Точно так же можно работать и с методами класса