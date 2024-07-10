import pathlib
from PIL import Image

def pth(pth):
    e = str(pathlib.Path(__file__)).split("\\")
    del e[-1]
    e = "/".join(e) + "/" + pth
    return e

def get_image_pixels(x):
    imgg = Image.open(x)
    width, height = imgg.size
    pixels = []
    for y in range(height):
        for x in range(width):
            pixels.append(imgg.getpixel((x, y)))
    return [pixels,height,width]

def create_image_from_pixels(image,name = "result.png",save = False):
    img = Image.new('RGBA', (image[2], image[1]))
    img.putdata(image[0])
    if save:
        img.save(pth(name))
    return img

img = get_image_pixels(pth("image.png"))

for i in range(len(img[0])):
    e = int((img[0][i][0] + img[0][i][1] + img[0][i][2])/3)
    r = img[0][i][0]-e
    g = img[0][i][1]-e
    b = img[0][i][2]-e
    img[0][i] = (int(e+(r*((i%img[2])/img[2]))),
                 int(e+(g*((i%img[2])/img[2]))),
                 int(e+(b*((i%img[2])/img[2]))))

create_image_from_pixels(img,save=True)