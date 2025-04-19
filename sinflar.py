class MATRITSA:
    def __init__(self, n, mat=None):
        self.n = n
        if mat:
            self.mat = mat
        else:
            # 0 bilan to'ldirilgan n x n matritsa
            self.mat = [[0 for _ in range(n)] for _ in range(n)]

    def input_matrix(self):
        print(f"{self.n}x{self.n} o‘lchamdagi matritsani kiriting:")
        for i in range(self.n):
            row = list(map(int, input(f"{i+1}-qator: ").split()))
            if len(row) != self.n:
                raise ValueError(f"Har bir qatorda {self.n} ta element bo‘lishi kerak.")
            self.mat[i] = row

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError("Matritsalar bir xil o‘lchamda bo‘lishi kerak.")
        result = MATRITSA(self.n)
        for i in range(self.n):
            for j in range(self.n):
                result.mat[i][j] = self.mat[i][j] + other.mat[i][j]
        return result

    def __mul__(self, other):
        if self.n != other.n:
            raise ValueError("Matritsalar bir xil o‘lchamda bo‘lishi kerak.")
        result = MATRITSA(self.n)
        for i in range(self.n):
            for j in range(self.n):
                result.mat[i][j] = sum(self.mat[i][k] * other.mat[k][j] for k in range(self.n))
        return result

    def transpose(self):
        result = MATRITSA(self.n)
        for i in range(self.n):
            for j in range(self.n):
                result.mat[i][j] = self.mat[j][i]
        return result

    def print_matrix(self, label="Matritsa"):
        print(f"\n{label}:")
        for row in self.mat:
            print(" ".join(map(str, row)))


# Test qilish
n = int(input("Matritsalar o‘lchamini kiriting (n): "))
print("\nA matritsasi:")
A = MATRITSA(n)
A.input_matrix()

print("\nB matritsasi:")
B = MATRITSA(n)
B.input_matrix()

# A + B
C = A + B
C.print_matrix("A + B")

# A * B
D = A * B
D.print_matrix("A * B")

# Transponirlangan A
AT = A.transpose()
AT.print_matrix("A ning transponirlangan ko‘rinishi (A^T)")
