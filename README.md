# stegosaurus
Steganography tool that hides text in pictures

## Requirements
Stegosaurus requires Pillow, a python image processing library. It can be installed 
on your system by running

    $ pip install Pillow
## Use

Stego.py is run with a message text file, and a png image file. The script encodes a 
bit of the message into pixels in an image. 

To retrieve the message, one can run desteg.py with the stego image. For now, 
desteg.py prints the output message to stdout.

This repo includes variation of stego that change different pixel values in different
ways. It also comes with sample images. However, only stego.py and desteg.py are needed.
