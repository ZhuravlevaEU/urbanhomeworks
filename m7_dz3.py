# Оператор with

class WordsFinder:
    file_names = []
    def __init__(self):
        self.

def custom_write(file, strings):
    file_name = 'text_k_zadache_7_3.txt'
    strings = info
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file_name:
        for string in strings:
            position = file_name.tell()
            file_name.write(string + '\n')
            strings_positions[(len(strings_positions) + 1, position)] = string
    return strings_positions

info = [
    'Если б не было учителя,',
    'То и не было б, наверное,',
    ' Ни поэта, ни мыслителя,',
    ' Ни Шекспира, ни Коперника.']




result = custom_write('text_k_zadache_7_3.txt', info)
for elem in result.items():
    print(elem)
