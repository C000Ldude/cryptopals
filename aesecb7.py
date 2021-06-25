from helper import *
ctfile=open('encoded7.txt','r')
ct=ctfile.read()

ctb64decoded=base64tobytes(ct)

bkey='YELLOW SUBMARINE'.encode()
bytespt=decryptAES(ctb64decoded,bkey)
print(bytespt.decode('utf-8'))
