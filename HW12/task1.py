import csv


class Descriptor:
    MIN_MARK, MAX_MARK = 2, 5
    MIN_TEST, MAX_TEST = 0, 100

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Invalid!")
        else:
            if value:
                if not (value[0].isupper() and value.isalpha()):
                    raise ValueError(f"Invalid {self.param_name}")
            else:
                raise ValueError('Invalid!')


class Student:
    surname = Descriptor()
    name = Descriptor()
    patronymic = Descriptor()

    def __init__(self, surname: str, name: str, patronymic: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._disciplines = []
        self.progress = {}
        self.initialize()

    def initialize(self):
        with open(f'disciplines.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self._disciplines.append(row[0])
                self.progress[row[0]] = [None, None]

    def get_mark(self, discipline: str, mark: int):
        if discipline not in self.progress:
            raise ValueError('Invalid!')
        else:
            if 2 <= mark <= 5:
                self.progress[discipline][0] = mark
            else:
                raise ValueError(f'Invalid!')

    def get_test_res(self, discipline: str, res: int):
        if discipline not in self.progress:
            raise ValueError('Invalid!')
        else:
            if 0 <= res <= 100:
                self.progress[discipline][0] = res
            else:
                raise ValueError(f'Invalid!')

    def get_average(self):
        average_mark, average_res = 0, 0
        mark_counter, res_counter = 0, 0

        for m_, r_ in self.progress.values():
            if m_ is not None:
                average_mark += m_
                mark_counter += 1
            if r_ is not None:
                average_res += r_
                res_counter += 1
        return average_mark / mark_counter, average_res / res_counter


s = Student("Ivanov123", "Ivan", "Ivanovich")
print(s.surname)
