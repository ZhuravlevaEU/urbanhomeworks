# Файлы в ОС
import os
import time

directory = os.getcwd()

def mkdir_second():
    if os.path.exists('second'):  # если папка second существует,то
        os.chdir('second')  # изменим текущий каталог на second
    else:
        os.mkdir('second')  # в противном случаем, создадим папку second на рfвне с текущей
        os.chdir('second')  # изменим текущий каталог на second
    os.makedirs(r'sortirovka/third/forth')  # создаем вложенные папки

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)  # переменной присваивается значение пути
        filetime = os.path.getmtime(filepath)  # переменной присваивается время последнего изменения файла
        # показывает текущую дату в формате
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)  # показывает размер файла
        parent_dir = os.path.dirname(filepath)  # показывает имя каталога-родителя
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {filetime}')

print(os.getcwd())  # определим абсолютный путь к рабочей директории
if os.path.exists('sortirovka/test_dir'):  # если папка test_dir существует,то
    os.chdir('sortirovka/test_dir')  # изменим текущий каталог на test_dir
    mkdir_second()
else:
    mkdir_second()

print(os.getcwd())  # определим абсолютный путь к рабочей директории
print(os.listdir())  # проверяем содержимое текущей директории
