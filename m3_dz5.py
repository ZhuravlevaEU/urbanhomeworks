# Рекурсивное умножение цифр
def get_multiplied_digits(number):
    if len(str_number) > 1:
        return str_number
    else:
        return number * get_multiplied_digits(int(str_number[number]))
    print(get_multiplied_digits(number))

number = 40203
str_number = str(int(number))
result = get_multiplied_digits(number)
print(result)
