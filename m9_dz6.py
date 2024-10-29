# Задание по етем "Генераторы"
from itertools import combinations

def all_variants(text):
    text = []
    for i in range(1, len(text)+1):
        b = combinations(text, i)
        list.extend(b)
        for j in list:
            j = list[j]
            yield (''.join(j))


a = all_variants("abcabc")
print(a)

for i in a:
    print(i)

