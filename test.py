import unittest

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



class TestStegMethods(unittest.TestCase):

    def test_stegStrToBits(self):
        self.assertEqual(strToBits(['h']),'01101000')
        self.assertEqual(strToBits(['he']),'0110100001100101')
        self.assertEqual(strToBits(['hello']),'0110100001100101011011000110110001101111')
        self.assertEqual(strToBits(['hello','world']),'01101000011001010110110001101100011011110111011101101111011100100110110001100100')

        self.assertEqual(strToBits(['hello\n','world\n']),"0110100001100101011011000110110001101111000011010000101001110111011011110111001001101100011001000000110100001010")

if __name__ == '__main__':
    unittest.main()
