import random

number = random.randint(3, 20)
print(number)
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
str = ''

for i in range(1, number):
    for j in range(i + 1, number):
        if number % (i + j) == 0:
            str = str[i] + str[j]
            print(number, '-', str)
        else:
            print('задача решена')
