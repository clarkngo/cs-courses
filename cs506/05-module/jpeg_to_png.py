from PIL import Image

img = Image.open('C:/Users/peini/OneDrive/Desktop/CityU/506/5/cs506-hos05-summer-2025-Penny967/bulldog.jpeg')
width, height = img.size
print("width:", width, "height:", height)

if img.format =='JPEG':
    img.save("bulldog2.png", "PNG")
    print("Image converted to PNG format.")