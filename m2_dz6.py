import random

number = random.randint(3, 20)
print(number)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 2

for i in list:
    if (list[i-2] + list[i-1]) % number == 0:
        print(list[i-2], list[i-1])
    else:
        i += 1
        continue
