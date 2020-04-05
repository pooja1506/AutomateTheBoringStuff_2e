from PIL import ImageColor , Image , os
ImageColor.getcolor('red', 'RGBA')

#Opening the image
catIm = Image.open('zophie.png')

#change the working directory
os.chdir('C:\\folder_with_image_file')

