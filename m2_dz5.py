# Задача "Матрица воплоти":
def get_matrix(n, m, value):
    n = int(input('Введите количество строк матрицы (2, 3, 4)')) - 1
    m = int(input('Введите количество столбцов матрицы (2, 5, 2)')) - 1
    value = int(input('Введите значение переменной (10, 42, 13)'))
    index1 = 0
    for index1 in range(n):
        # добавляю пустой список в matrix
        matrix = []
        index2 = 0
        for index2 in range(m):
            matrix = [n, m, value]
            break
        break
    print(matrix)
    return n, m, value

n = int(input('Введите количество строк матрицы (2, 3, 4)')) - 1
m = int(input('Введите количество столбцов матрицы (2, 5, 2)')) - 1
value = int(input('Введите значение переменной (10, 42, 13)'))
get_matrix(n, m, value)
