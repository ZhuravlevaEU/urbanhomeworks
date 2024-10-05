# Режим открытия файлов

class Product:
    def __init__(self, name, weight, category):
        self.product = name # имя
        self.weight = weight # вес
        self.category = category # категория товара

    def __str__(self):
        print(f'{self.product}, {self.weight}, {self.category}')

class Shop(Product):
    __file_name = 'products.txt'
    def __init__(self):
        pass

    def get_products(self):
        file = open(self.__file_name, 'r', encoding = 'utf-8')
        print(self.__file_name.readablle()) # проверим, можно прочитать файл
        self.__file_name.close()
        print(f'{self.product}, {self.weight}, {self.category}')

    def add(self, *products):
        file.open(self.__file_name, 'w')
        print(self.__file_name)
        if self.product in self.__file_name:
            pprint(self.__file_name.writ('\n*products'))
        else:
            print(f'Продукт {self.product} уже есть в магазине')
        self.__file_name.close()
        print(self.__file_name)



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
