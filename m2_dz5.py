# Задача "Матрица воплоти":

def get_matrix(n, m, value):
    result1 = get_matrix(2, 2, 10)
    result2 = get_matrix(3, 5, 42)
    result3 = get_matrix(4, 2, 13)
    matrix = []
    index1 = 0
    for index1 in n:
        # добавьте пустой список в matrix???
        matrix1 = [matrix]
        index2 = 0
        for index2 in m:
            matrix1 = [value]
            get_matrix(n, m, value)
            break
        break
# верните значение переменной matrix?????
print(result1)
print(result2)
print(result3)
