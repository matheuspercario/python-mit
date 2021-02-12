# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 12th, 2021
# ============================================================================


class Matrix:

    # Constructor
    def __init__(self, matrix):
        lines = []
        for e in matrix:
            if len(e) != len(matrix[0]):
                lines.append(False)
            else:
                lines.append(True)
        # Condição
        if all(lines):
            self.matrix = matrix
        else:
            self.matrix = None

    # Methods
    def size(self):
        numrows = len(self.matrix)
        numcols = len(self.matrix[0])
        return numrows, numcols

    def get(self, r, c):
        nrows, ncols = self.size()
        if 0 <= r < nrows and 0 <= c < ncols:
            return self.matrix[r][c]
        else:
            return None

    def set(self, r, c, val):
        nrows, ncols = self.size()
        if 0 <= r < nrows and 0 <= c < ncols:
            self.matrix[r][c] = val
        else:
            return None

    def row(self, n):
        nrows = self.size()[0]
        if 0 <= n < nrows:
            return list(self.matrix[n])

    def col(self, n):
        ncols = self.size()[1]
        if 0 <= n < ncols:
            return [line[n] for line in self.matrix]

    def transpose(self):
        nrows, ncols = self.size()
        return Matrix([self.col(n) for n in range(ncols)])

    # stranger methods
    def add(self, other):
        if isinstance(other, Matrix):
            if self.size() != other.size():
                return None

            return Matrix([[c_s + c_o for c_s, c_o in zip(l_s, l_o)] for l_s, l_o in zip(self.matrix, other.matrix)])

        elif isinstance(other, (int, float)):
            return Matrix([[element + other for element in lin] for lin in self.matrix])

    def sub(self, other):
        if isinstance(other, Matrix):
            if self.size() != other.size():
                return None

            return Matrix([[c_s - c_o for c_s, c_o in zip(l_s, l_o)] for l_s, l_o in zip(self.matrix, other.matrix)])

        elif isinstance(other, (int, float)):
            return Matrix([[element - other for element in lin] for lin in self.matrix])

    def mul(self, other):
        if isinstance(other, Matrix):
            nrows_self, ncols_self = self.size()
            nrows_other, ncols_other = other.size()
            if ncols_self != nrows_other:
                return None

            result = [[0] * ncols_other for line in range(nrows_self)]
            print(result)
            for i in range(nrows_self):
                for j in range(ncols_other):
                    for k in range(nrows_other):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]

            return Matrix(result)

        elif isinstance(other, (int, float)):
            return Matrix([[element * other for element in lin] for lin in self.matrix])

    # Dunder methods
    def __str__(self):
        if self.matrix is None:
            return "MatrixError: Inconsistent number of columns"
        out = 'MATRIX\n'
        for lin in self.matrix:
            out += "| "
            for col in lin:
                out = out + str(col) + " "
            out += "|\n"

        return out

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)


m = Matrix([[2, 3], [0, 1], [-1, 4]])
n = Matrix([[1, 2, 3], [-2, 0, 4]])
# print(m)
# print(m.size())
# print(m.get(-1, 0))
# m.set(1, 2, 10)
# print(m)
# print(m.row(1))
# print(m.col(1))
# m_t = m.transpose()
# print(m_t)
# print(m)
# print(n)
# print(m * n)
