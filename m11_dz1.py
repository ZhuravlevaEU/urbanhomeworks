import os, sys
from PIL import Image

print(im.format, im.size, im.mode)
PPM (512, 512)
RGB
im.open(capitain)

# Конвертируйте файлы в JPEG
for infile in sys.argv[1:]:
    f, e = os.path.capitain(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)

# Создание миниатюр в формате JPEG
size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.capitain(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)

# Идентификация файлов изображений
for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass

# Вырезание, вставка и объединение изображений
# Копирование подпрямоугольника из изображения
# Область определяется 4-кортежем, координаты — (левая, верхняя, правая, нижняя)
box = (0, 0, 64, 64)
region = im.crop(box)
# Обработка подпрямоугольника и вставка его обратно
region = region.transpose(Image.Transpose.ROTATE_180) # область, транспонировать, поворот 180 град
im.paste(region, box) # вставить область прямоугольник

