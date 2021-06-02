from PIL import Image
from PIL import ExifTags
import sys

def effect_intensity(im, f):
    new_im = im.convert("YCbCr")

    width, height = im.size
    
    for x in range(width):
        for y in range(height):
            pixel = new_im.getpixel( (x,y) )
            py = min(255, int(pixel[0] * f)) # [0] is the Y channel
            new_im.putpixel( (x,y), (py, pixel[1], pixel[2]) )

    return new_im


def main(fname):
    im = Image.open(fname)
    f = float(input("Qual o factor que deseja? "))
    new_im = effect_intensity(im, f)

    new_im.save(fname + "-int.jpg")
    
    print("Done!")

main(sys.argv[1])