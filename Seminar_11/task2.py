class Archive:
    list_archive = None

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if cls.list_archive is None:
            cls.list_archive = super().__new__(cls)
            cls.list_archive.string = []
            cls.list_archive.digit = []
        else:
            cls.list_archive.string.append(cls.list_archive.name)
            cls.list_archive.digit.append(cls.list_archive.age)
        return cls.list_archive

    def __str__(self):
        return f'{self.name = }\n{self.age = }\n'

    def __repr__(self):
        return str(self)


a = Archive('name', 5)
b = Archive('baby', 7)
print(b.list_archive.string)
print(b.list_archive.digit)
print(a, b)
