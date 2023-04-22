from HW13.task1 import *


class Matrix:
    def __init__(self, matrix: list[list[int]]):
        set_ = set()
        for row in matrix:
            set_.add(len(row))
            if len(set_) > 1:
                raise ShapeMatrixError("Invalid!")
        self.matrix = matrix

    def check_size(self, other: 'Matrix'):
        return len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])

    def core(self, other: 'Matrix', sing_plus: bool = True):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatrixAdditionsSubtractionError('Must have the same sizes')
        return Matrix(
            [[self.matrix[j][i] + (1 if sing_plus else -1) * other.matrix[j][i] for i in range(len(self.matrix[0]))] for
             j in range(len(self.matrix))])

    def __add__(self, other: 'Matrix'):
        return self.core(other)

    def __sub__(self, other: 'Matrix'):
        return self.core(other, False)

    def __eq__(self, other: 'Matrix'):
        if not self.check_size(other):
            return False
        for j, row in enumerate(self.matrix):
            for i, el in enumerate(row):
                if el != other.matrix[j][i]:
                    return False

        return True

    def __ne__(self, other: 'Matrix'):
        return not (self == other)

    def __mul__(self, other: 'Matrix'):
        if (k := len(self.matrix[0])) != len(other.matrix):
            raise MatrixMultiplicationError(f'Invalid')
        j, i = len(self.matrix), len(other.matrix[0])
        product = [[0 for _ in range(i)] for _ in range(j)]
        for j_ in range(j):
            for i_ in range(i):
                for k_ in range(k):
                    product[j_][i_] += self.matrix[j_][k_] * other.matrix[k_][i_]
        return Matrix(product)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __repr__(self):
        return str(self)


mat = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat1 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
mat3 = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
mat4 = Matrix([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
mat2 = mat * mat1
print(f'res: \n{mat2}')
mat_ = mat + mat1
print(f'res: \n{mat3}')
mat_1 = mat - mat1
print(f'res: \n{mat4}')

# ShapeMatrixError
mat_2 = Matrix([[1, 2, 3], [1, 2], [1, 1, 2, 4]])

# MatrixAdditionsSubtractionError
mat_3 = mat + mat3

# MatrixMultiplicationError
mat_4 = mat * mat4
