from helper import keyxor, singlebytexor


msg='Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'

#converting msg to bytes
bytemsg=msg.encode()

#converting key to bytes
bkey='ICE'
bytekey=bkey.encode()

#applying xor operation between bytemsg and bytekey and return result is byte
result=keyxor(bytemsg,bytekey)

print(result)

print(bytes.hex(result))









