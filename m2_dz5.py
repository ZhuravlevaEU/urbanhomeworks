# Задача "Матрица воплоти":
def get_matrix(n, m, value):
    matrix = []
    index1 = 0
    for index1 in n:
        # добавьте пустой список в matrix???
        index2 = 0
        for index2 in m:
            matrix = [value]
            get_matrix(n, m, value)
            print(matrix)
            break
        break
    return n, m, value

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
