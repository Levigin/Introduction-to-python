class Animals:
    def __init__(self, name: str, age: int, weight: int):
        self.name = name
        self.age = age
        self.weight = weight

    def sound(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name = }, {self.age = }, {self.weight = }'

    def __repr__(self):
        return str(self)

    def give_birth(self, other: 'Animals'):
        return Animals(f'{self.name}_{other.name}', 0, 2)


class Fish(Animals):
    def __init__(self, name: str, age: int, weight: int, fins: int):
        self.fins = fins
        super().__init__(name, age, weight)
        self.swim()

    def swim(self):
        print(f'I am swimming')


class Birds(Animals):
    def __init__(self, name: str, age: int, weight: int, is_fly: bool):
        self.is_fly = is_fly
        super().__init__(name, age, weight)
        self.fly()

    def fly(self):
        if self.is_fly:
            print(f'I am flying')
        else:
            print(f'Sorry(')


class Mammals(Animals):
    def __init__(self, name: str, age: int, weight: int, legs: int):
        self.legs = legs
        super().__init__(name, age, weight)
        self.run()

    def run(self):
        print(f'I am running')


class Factory:
    args_ = None

    def __init__(self, *args):
        Factory.args_ = args

    def __new__(cls, *args):
        return args[0](*args[1:])


f = Factory(Fish, 'Karasь', 10, 10, 5)
print(f)