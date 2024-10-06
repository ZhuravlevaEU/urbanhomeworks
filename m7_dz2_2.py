# Позиционирование в файле
def custom_write(file, strings):
    file_name = 'text_k_zadache_7_3.txt'
    strings = info
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    if string in range(info):
        position = file_name.tell()
        file_name.write(string + '\n')
        strings_positions[(len(strings_positions) + 1, position)] = string




info = [
    'Если б не было учителя,',
    'То и не было б, наверное,',
    ' Ни поэта, ни мыслителя,',
    ' Ни Шекспира, ни Коперника.']

result = custom_write('text_k_zadache_7_3.txt', string_position)
for elem in result.items():
    print(elem)
