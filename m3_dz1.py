calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

str = input('Введите слово: ')
list(str)

def string_info(str):
    count_calls()
    a = len(str)
    b = str.upper()
    c = str.lower()
    return a, b, c

el = input('Введите строку: ')

def is_contains(str, seach_list):
    count_calls()
    str = str.lower()
    for el in seach_list:
        if el.lower() == str:
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
