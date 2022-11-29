class User:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return bool(self.value)

    def __bytes__(self):
        return str(self.value).encode()
        #Или так bytes(int(self.value))

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)


a = User(1.256)

print(bool(a))
print(bytes(a))
print(float(a))
print(int(a))