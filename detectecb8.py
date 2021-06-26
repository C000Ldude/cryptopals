from helper import *

txtrd=open('encoded8.txt','r')

#creating a list of the hex splitted at newline characters
pt=txtrd.read().split('\n')


#dictionary to save the count(hex and number of repetitions of bytes in different blocks of the hex)
countdict={}


for i in range(len(pt)-1):
    #changing the hex from list to byte
    msg1=hextobytes(pt[i])

    #numver of chunks to divide the total text into( in ECB the plaintext is divided normally into blocks of 16 bytes each)
    keysize=16

    #creating blocks
    blocks=[]

    for j in range(10):
        blocks.append(msg1[j*keysize:j*keysize+16])


    count=0

    #counting the repetitions in the bytes between different blocks of a ciphertext
    for j in range(9):
        for k in range(j,10):
            if j!=k:
                result=hammingdis(blocks[j],blocks[k])
                samebits=128-result
                count+=samebits

    countdict[pt[i]]=count

#sorting the dictionary in ascending order to get the ciphertext with the highest number of repetitions which is our answer
print(sorted(countdict.items(),key=lambda i:i[1]))
print('the hex with ECB:   ',sorted(countdict.items(),key=lambda i:i[1])[203])

#'d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a', 3362




