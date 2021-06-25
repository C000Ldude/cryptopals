from helper import *

hexval='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(hexval)

#conversion of hex to byte
byteval=hextobytes(hexval)

#conversion of byte to base64
base64val=bytestobase64(byteval)

#printing the output in utf-8
print(base64val.decode('utf-8'))