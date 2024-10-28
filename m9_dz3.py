# Генераторные сборки

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторные сборки:
# высчитывает разницу длин строк из списков first и second
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))

# содержит результаты сравнения длин строк в одинаковых позициях из списков first и second
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))


print(list(first_result))
print(list(second_result))
