# Задача "Нули ничто, отрицание недопустимо!"
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
my_list_1 = []
while index < len(my_list):
    if my_list[index] > 0:
        my_list_1.append(my_list[index])
        print(my_list_1[index])
        index += 1
        continue
    else:
        break
