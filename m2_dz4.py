# Цикл for. Элементы списка
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for index in numbers:
    if index < 2:
        continue

    for j in range(2, index):
        if index % j != 0:
            primes.append(index)
            print(primes)
            break
    else:
        not_primes.append(index)
        print(not_primes)


