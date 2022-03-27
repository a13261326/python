from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        l = 0
        for x in self.matrix:
            l = l + len(x)

        if l % len(self.matrix) != 0:
            raise ValueError('fail initialization matrix')

    def __str__(self) -> str:
        c = []
        for line in self.matrix:
            c.append(f'|{" ".join(map(str, line))}|')

        return '\n' "".join(map(str, c))

    def __add__(self, other):
        d = [[int(self.matrix[line][i]) + int(other.matrix[line][i])
              for i in range(len(self.matrix[line]))]for line in range(len(self.matrix))]
        return Matrix(d)



if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(second_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    #fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
#     """

#     def __str__(self) -> str:
#         return f'Пузырь объемом {self.volume} ({"пустой" if self.empty else "полный"})'
#
#     def __add__(self, other):
#         volumes = self.volume + other.volume
#         print(self)
#         print(other)
#         print(f'Прикинув в уме сумму объёмов этих пузырей, получился литраж равный {volumes}')
#         # перегрузка операторов обычно должна всегда отдавать новый объект этого же класса
