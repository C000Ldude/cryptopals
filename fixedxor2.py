from helper import *

hex1='1c0111001f010100061a024b53535009181c'
hex2='686974207468652062756c6c277320657965'
print(hex1)
print(hex2)

#conversion of hex to bytes
byte1=hextobytes(hex1)
byte2=hextobytes(hex2)

#doing the XOR between characters of byte1 and byte2
result=fixedxor(byte1,byte2)
print(result.hex())