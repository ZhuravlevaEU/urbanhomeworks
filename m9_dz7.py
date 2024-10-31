# задание по теме "Декораторы"
def decorator(func):
    def wrapper(*args: int): # функция-обложка
        result = func(*args)
        for div in range(2, result):
            if result % div == 0:
                print(f'Составное')
                break
            else:
                print(f'Простое')
    return wrapper
@is_prime
def sum_three(first, second, third):
    print(first+second+third)
    return first+second+third

result = sum_three(2, 3, 6)
print(result)
