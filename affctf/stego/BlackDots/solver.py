from PIL import Image

img = Image.open("image.png")
img = img.convert('RGB')

flag = ""

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if img.getpixel((x, y)) == (255, 255, 255):
            flag += "1"
        else:
            flag += "0"
           

print(flag)
