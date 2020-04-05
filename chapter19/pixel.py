from PIL import Image
im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

from PIL import ImageColor
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
im.getpixel((0, 0))
im.getpixel((0, 50))
im.save('putPixel.png')