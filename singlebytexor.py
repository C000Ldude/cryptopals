from helper import *

hexmessage='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
print(hexmessage)

#conversion of hex to byte
bytemessageorg=hextobytes(hexmessage)

#finding the key used for xoring ciphertext
ky=chr(bruteforcechrs(bytemessageorg))

print(ky)
