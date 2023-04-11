from time import time


class MyString(str):

    def __new__(cls, name, value):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.value = value
        return instance

    def __str__(self):
        return f'{self.name = }, {self.value = }'


a = MyString('bob', 'tom')
print(a.upper)

