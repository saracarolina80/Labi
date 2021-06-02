from PIL import Image
from PIL import ExifTags
import sys

def gammaCorrection(im ,y ,g ,f):

    # y -> valor do canal
    # g -> fator de correção gamma 
    #  f -> fator de normalização     ( f = m / m**g )
    # m -> valor máximo de intensidade ( normalmente 255)
    m = 255
    new_im = im.convert("YCbCr")

    
    width, height = im.size
    
    for x in range(width):
        for y in range(height):
            pixel = new_im.getpixel( (x,y) )
            f = m / m**g
            py = min(255, int(y**g * f)) # [0] is the Y channel
            new_im.putpixel( (x,y), (py, pixel[1], pixel[2]) )

    return new_im


def main(fname):
    im = Image.open(fname)
    y = float(input("Qual o valor de canal que deseja? "))
    g = float(input("Qual o fator de correção que deseja? "))
    f = float(input("Qual o fator de normalização que deseja? "))
    new_im = gammaCorrection(im ,y,g,f)

    new_im.save(fname + "-gamma.jpg")
    
    print("Done!")

main(sys.argv[1])