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
    if (len(sys.argv)<4):
        raise NameError( "Correct Usage: stego.py <medium image> <secretMessage.txt>")
    medium = sys.argv[1]
    source = sys.argv[2]
    stego_name = sys.argv[3]
    sourceFile = file(source,'r')
    print "reading image file"
    medium_pic = Image.open(medium,'r')
    width,height = medium_pic.size
    pixel_values = list(medium_pic.getdata())
    print "reading secret into file" 
    strings = sourceFile.readlines()
    
    stego_image = Image.new('RGB',(width,height),"black")
    # create a new black image
    stego_array = stego_image.load()
    
    # Turn the file into a bitstring
    print "converting file into bitstring"
    strings.append('eoftm')
    bitString = strToBits(strings)
    print bitString
    print "embedding secret into medium" 
    for i in range(len(pixel_values)):
        try:
            (a,b,c,d) = pixel_values[i]
        except ValueError:
            (a,b,c) = pixel_values[i]
        try:
            if bitString[i]=='1':
                stego_array[i%width,i/width] = (a|0x01,b,c)
            else:
                stego_array[i%width,i/width] = (a&0xfe,b,c)
        except IndexError:
            stego_array[i%width,i/width] = (a,b,c)
    stego_image.save(stego_name,"png")
    


