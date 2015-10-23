import sys
from PIL import Image

def strToBits(strings):
    bitString=''
    for string in strings:
        for letter in string:
            binary = bin(ord(letter))[2:]
            # Insert 0s to make it an 8 digit binary number
            numZ = 8-len(binary)
            bits = '0'*(8-len(binary))+binary
            bitString+=bits
    return bitString


if __name__ == '__main__':
    medium = sys.argv[1]
    source = sys.argv[2]
    sourceFile = file(source,'r')
    im = Image.open(medium,'r')
    width,height = im.size
    pixel_values = list(im.getdata())
    
    strings = sourceFile.readlines()
    
    one = Image.new('RGB',(width,height),"black")
    # create a new black image
    original = Image.new('RGB',(width,height),"black")
    copy = original.load()
    p1 = one.load()
    
    # Turn the file into a bitstring
    strings.append('eoftm')
    print strings
    bitString = strToBits(strings)
    print bitString 
    
    for i in range(len(pixel_values)):
        try:
            (a,b,c,d) = pixel_values[i]
        except ValueError:
            (a,b,c) = pixel_values[i]
        copy[i%width,i/width] = (a,b,c)
        try:
            if bitString[i]=='1':
                p1[i%width,i/width] = (a|0x80,b,c)
            else:
                p1[i%width,i/width] = (a&0x7f,b,c)
        except IndexError:
            p1[i%width,i/width] = (a,b,c)
    one.show()
    one.save(source[:-4] + medium[:-4]+"StegMSB.png","png")
    im.show()
    original.show()
    


