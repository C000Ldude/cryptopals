from helper import *

#extracting all the hex values from the file
encoded=open("encoded.txt",'r')
words=encoded.read().splitlines()

for i in range(0,len(words)):
    #changing the hex to byte
    byteop=hextobytes(str(words[i]))

    #finding the byte value of the key used for xor
    bytehighfreqchar=chr(bruteforcechrs(byteop)).encode()

    #doing the XOR operation of byteop with bytehighfreqchar
    result=singlebytexor(byteop,bytehighfreqchar)

    print(i,'   ',result.decode('utf-8','ignore'))