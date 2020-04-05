from PIL import Image
catIm = Image.open('zophie.png')
catIm.size
width, height = catIm.size
print(width)
print(height)
catIm.filename
catIm.format
catIm.format_description
catIm.save('zophie.jpg')