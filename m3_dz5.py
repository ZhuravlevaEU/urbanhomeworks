# Рекурсивное умножение цифр
def get_multiplied_digits(n):
    if len(str_n) > 1:
        return str_n
    else:
        return n * get_multiplied_digits(int(str_n[n]))
    print(get_multiplied_digits(n))

n = (1, 2, 3, 4, 5, 6, 7, 8, 9)
str_n = int(n)
result = get_multiplied_digits(40203)
print(result)

