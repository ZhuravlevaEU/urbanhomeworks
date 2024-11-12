import os, sys
from PIL import Image



filename = "cat.jpg"
with Image.open("cat.jpg") as img: # открываем файл
    img.load() # чтения в память, чтобы теперь файл можно было закрыть файл

img.show()

print(img.format, img.size, img.mode)
type(img)
print(isinstance(img, Image.Image)) # True
# кадрируем - вырезаем область
# левый верхний и правый нижний углы вырезаемой области
cropped_img = img.crop((300, 150, 700, 1000))
# возвращаем полученное изображение размером 400х850
cropped_img.show()
(400, 850)
# сжимаем область (фрагмент) в 4 раза (с доп.параметрами) и возвращаем изображение
low_resize_img = cropped_img.resize((cropped_img.width // 4, cropped_img.height // 4))
# масштабируем другим способом и возвращаем изображение
low_resize_img.show(4)
# сохраняем полученный рисунок
cropped_img.save("cropped_image.jpg")
low_resize_img.save("low_resolution_cropped_image.png")
# поворот исходного изображения
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.show()
# ротация на произвольный угол
rotated_img = img.rotate(45)
rotated_img.show()

# использовала стаью https://habr.com/ru/articles/681248/
