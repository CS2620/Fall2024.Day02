from PIL import Image

print(1<<8)

image = Image.open("car.jpg")

data = image.load()
print(image.width)
print(image.height)

for y in range(image.height):
    for x in range(image.width):
        pixel = data[x,y]

        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        red_factor = .21
        green_factor = .71
        blue_factor = .08
        
        k = int(red * red_factor + green * green_factor + blue * blue_factor)

        # v = max(red, green, blue)

        # k = v

        if(blue > 150):
            data[x,y] = (red,green,blue)
        else:
            data[x,y] = (k, k, k)

image.save("aye-aye.png")
