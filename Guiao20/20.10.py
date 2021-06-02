from PIL import Image
from PIL import ExifTags
import sys

def main(fname):
    im = Image.open(fname)
    new_im = Image.new(im.mode, im.size)

    width, height = new_im.size

    for x in range(width):
        for y in range(height):
            p = im.getpixel( (x,y) )
            r = 255-p[0]
            g = 255-p[1]
            b = 255-p[2]
            new_im.putpixel((x,y), (r, g, b) )
    
    new_im.save(fname + "-negativa.jpg")

main(sys.argv[1])