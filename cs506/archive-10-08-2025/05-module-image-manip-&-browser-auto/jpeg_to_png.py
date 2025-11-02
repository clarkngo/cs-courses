from PIL import Image

img = Image.open('bulldog.jpeg')
width, height = img.size
print("Width:", width, "Height:", height)

if img.format == 'JPEG':
    img.save('bulldog2.png')