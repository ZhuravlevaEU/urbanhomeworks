# Оператор with

class WordsFinder:
    def __init__(self, *file_names):  # неограниченное число Объектов класса
        self.file_names = file_names  # запишем объекты в список

    def get_all_words(self):  # - создаем cловарь
        all_words = {}  # формируем пустой словарь
        l = ""
        for file_name in self.file_names:
            # перебераем названия файлов и открываем каждый из них
            with open(file_name, 'r', encoding='utf-8') as file:
                line = file.read().lower()  # считывая строки переводим все символы в нижний регистр
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(punctuation, '')  # удаляем знаки препинания из строки
                words = line.split()  # разделяем строку на части по пробелам
                all_words[file_name] = words  # запишем в словарь полученные слова, где ключ — название файла,
                # а значение — список из слов этого файла
                print(all_words[file_name])  # печать значения по ключу
        return all_words

    def find(self, word):  # метод возвращает словарь, где word - искомое слово, где ключ - название файла,
        # значение - позиция первого такого слова в списке слов этого файла;
        dict_ = {}  # создаем словарь
        # перебираем по ключу (названию) и значению (списоку слов);
        for name, words in self.get_all_words().items():
            # item() - одновременная итерация
            # если строка содержит слово
            if word.lower() in words:
                # значение ключа словаря установим в индекс слова в списке слов, увеличенный на 1****
                dict_[name] = words.index(word.lower()) + 1
                # возвращаем словарь, где ключ - название файла, значение - позиция первого такого
                # слова в списке слов этого файла
        return dict_

    def count(self, word):  # метод возвращает словарь, где word - искомое слово, ключ - название файла,
        # значение - количество слов wordв списке слов этого файла
        dict_ = {} # создаем словарь
        for name, words in self.get_all_words().items():  # перебираем по ключу (названию) и значению (списоку слов)
            # значение ключа словаря установим в индекс слова в списке слов, увеличенный на 1****
            dict_[name] = words.count(word.lower())
            # возвращаем словарь, где ключ - название файла, значение - позиция первого такого
            # слова в списке слов этого файла
        return dict_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
