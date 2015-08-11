import sys
from PIL import Image

steg = sys.argv[1]

image = Image.open(steg,'r')
pixels = list(image.getdata())
bitString = ''
for (red,green,blue) in pixels:
    if ( red & 0x01 ) == 1:
        bit = '1'
    else:
        bit ='0'
    bitString += bit
message = ''
lense = ''
while lense != 'eoftm':
    byte = bitString[:8]
    message += chr(int(byte,2))
    try:
        lense = message[-5:]
    except IndexError:
        lense = ''
    bitString = bitString[8:]
print message
