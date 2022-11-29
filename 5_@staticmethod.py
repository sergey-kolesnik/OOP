class User:
    def __init__(self, name='name1', age=20):
        self.name = name
        self.age = age

    def get_data(self):
        print(self.name)
        print(self.age)

    #Декоратор делает метод статическим:
    @staticmethod
    def get_sum(x, y):
        print(x + y)

#Мы можем вызывать напрямую статический метод,
# без создания экземпляра класса,
# обращаясь к классу

User.get_sum(1, 3)

#Можем вызывать статикметод через созданный экземпляр класса:
a = User()
a.get_sum(5, 6)