class Vector:

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Vector({self._x}, {self._y})"

    def __repr__(self):
        return str(self)

    # def __getattribute__(self, value):
    #     return object.__getattribute__(self, value)
    #
    # def __setattr__(self, key, value):
    #     self.key = value
    #     return object.__setattr__(self, key, value)


v = Vector(2, 2)
print(getattr(v, '_x'))
