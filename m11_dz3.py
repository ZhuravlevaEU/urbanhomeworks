# Задание по теме "Интроспекция"
# Пример 1 - Изучаем свойства объектов с помощью интроспекции


from pprint import pprint
from inspect import getmodule

"""def introspection_info(obj):
   return {
        'type': type(obj).__name__,
        'attributes': obj.__dict__,
        'methods': dir(obj),
        'modul': getmodule(obj)
    }
class MyClass: # Проверим пустой класс
    pass

obj = MyClass()

number_info = introspection_info(obj)
print(number_info)"""

# Пример 2 - # Исследуем класс с объектом

"""def introspection_info(MyClass):
   return {
        'type': type(MyClass).__name__,
        'attributes': MyClass.__dict__,
        'methods': dir(MyClass),
        'modul': getmodule(MyClass)
   }
   
class MyClass:
    def __init__(self, age, name): # создадим объект
        self.age = age
        self.name = name

# выведем на экран созданный объект
    def print_user(self):
        return f"Меня зовут {self.name} мне {self.age} лет"


example = MyClass(20,'Lin')
print(type (example)) # проверяем тип объекта
print(dir(example.print_user())) # вызываем методы и атрибуты
print(example.__dict__) # вызываем атрибуты"""


# Пример 3 - # Исследуем
def introsp_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    attrs = [attr for attr in attributes if not callable(getattr(obj, attr))]
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__

    introsp_info = {'type': obj_type, 'attributes': attrs,
                         'methods': methods, 'module': module}

    return introsp_info


info = introsp_info(42)
pprint(info)
