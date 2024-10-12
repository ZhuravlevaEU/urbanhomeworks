# Try \ Except
# Реализуйте следующую функцию, которая будет складывать ДВА числа(int, float) и строки(str)

number_01 = None
number_02 = None

def add_everything_up(number_01, number_02):
    try:
        sum_numbers = number_01 + number_02
    except TypeError as exc:
        if not (number_01 and number_02):
            f_string = f'Отсутствует по крайней мере 1 аргумент - {exc} :{number_01} {number_02}'
        else:
            f_string = f'{number_01}{number_02}'
    else:
        f_string = sum_numbers
    return f_string


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
