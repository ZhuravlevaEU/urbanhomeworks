# Все ли равны?
fist=int(input('Введите первое число: '))
second=int(input('Введите второе число: '))
third=int(input('Введите третье число: '))
if fist == second and fist == third and second == third :
    print('Все числа равны')
elif fist == second or second == third or fist == third:
    print('Только 2 числа равны')
else :
    print('Все числа разные')
