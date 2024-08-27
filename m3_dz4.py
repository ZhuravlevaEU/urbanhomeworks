# Задача "Однокоренные" (произв число параметров

def single_root_words(root_word, *other_words):
    if root_word in other_words or other_words in root_word:
        same_words = []
        print(same_words)
    else:

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
