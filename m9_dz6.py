# Задание по етем "Генераторы"
from itertools import combinations

def all_variants(text):
    for i in range(len(text)):
        for j in range(i, len(text)):
            yield text[i: j+1]


a = all_variants("abc")
print(a)

for i in a:
    print(i)

