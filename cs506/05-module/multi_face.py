from PIL import Image

def multi_face():
    img = Image.open('C:/Users/peini/OneDrive/Desktop/CityU/506/5/cs506-hos05-summer-2025-Penny967/bulldog2.png')
    width, height = img.size
    resize = img.resize((width // 4, height // 4))
    
    flip = resize.transpose(Image.FLIP_LEFT_RIGHT)
    fwidth, fheight = flip.size

    pattern = Image.new('RGB', (590, 428), 'green')

    w, h = pattern.size
    for left in range(0, w, fwidth):
        for top in range(0, h, fheight):
            pattern.paste(flip, (left, top))

    pattern.save("multiface.png")

if __name__ == "__main__":
    multi_face()
    print("Multi-face image created and saved as 'multiface.png'.")