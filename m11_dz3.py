# Задание по теме "Интроспекция"
# Пример 1 - Изучаем свойства объектов с помощью интроспекции
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
print(example.print_user())
print(example.__dict__)
number_info = introspection_info(MyClass)
print(number_info)"""

# Пример 3 - # Исследуем
def introspection_info(obj):
    obj.type = type(obj).__name__
    attributes = dir(obj)
    result = [attr for attr in attributes if not callable(getattr(obj, attr))]
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__moduie__

    introspection_info(obj) = {'type': type(obj), 'attributes': result,
        'methods': methods, 'modul': module}

    return introspection_info

number_info = introspection_info(42)
print(number_info)
