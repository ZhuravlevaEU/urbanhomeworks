# Позиционирование в файле
def custom_write(file_name, strings):
    file_name = 'text_k_zadache_7_3.txt'
    strings = info
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(len(strings_positions) + 1, position)] = string
    return strings_positions

info = [
    'Если б не было учителя,',
    'То и не было б, наверное,',
    ' Ни поэта, ни мыслителя,',
    ' Ни Шекспира, ни Коперника.']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

