calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

str = input('Введите слово прописными буквами: ')
list(str)

def string_info(str):
    count_calls()
    a = len(str)
    b = str.upper()
    c = str.lower()
    return a, b, c

el = input('Введите строку: ')
i = 0

def is_contains(str, el):
    count_calls()
    str = str.lower()
    for el in el:
        if el.lower() == str:
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
