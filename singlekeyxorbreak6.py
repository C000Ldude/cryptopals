from helper import *

txtrd=open('encoded6.txt','r')
pt=txtrd.read()


msg1=base64tobytes(pt)



#creating keysize list
keysize=[]
for i in range(2,30):
    keysize.append(i)

hammingdisdict={}



#finding the keysizes with the smallest normalised edit distance
for i in keysize:
    count=[]
    msgbytes=[]
    for j in range(50):
        msgbytes.append(msg1[j*i:(j+1)*i])


    for k in range(len(msgbytes)-1):
            count.append(hammingdis(msgbytes[k],msgbytes[k+1]))

    hammingdisdict[i]=round(sum(count)/i,3)


#sorting the keysizes by their hamming distance
sortedhammingdis=sorted(hammingdisdict.items(),key=lambda x:x[1])



#the first three keysizes with the smallest normalised edit distance
selectedkeysize=[sortedhammingdis[0][0],sortedhammingdis[1][0],sortedhammingdis[2][0]]

#selected key sizes
print('Selected key sizes :  ',selectedkeysize)

#creating blocks
blocks=[]


for i in range(3):
    block=[]
    lengthfromtotal=1500
    noblocks=int(lengthfromtotal/selectedkeysize[i])
    if lengthfromtotal%selectedkeysize[i]!=0:
        noblocks+=1
    for j in range(noblocks):
        temp=bytes()
        for k in range(selectedkeysize[i]):
            index=j*selectedkeysize[i]+k
            if index<lengthfromtotal:
                temp+=chr(msg1[index]).encode()
        block.append(temp)

    blocks.append(block)


trnblocks=[]
trnblockslength=[]




#transponse creation
for i in range(len(blocks)):


    blocklen=len(blocks[i][0])
    trnblock=[]



    for k in range(blocklen):
        bytetrn=bytes()
        for j in range(len(blocks[i])-1):
            bytetrn+=chr(blocks[i][j][k]).encode()
        trnblock.append(bytetrn)

    trnblocks.append(trnblock)




for i in range(len(trnblocks)):
    print('\n\nkeys resulting from keysize selection: ',i)
    for block in trnblocks[i]:
        #finding the keys from each block
        bytehighfreqchar=chr(bruteforcechrs(block)).encode()

        print(bytehighfreqchar.decode('utf-8'),end='')


#Decoding the encoded ciphertext with key obtained
print('\n\nDecoded Text\n\n')

print(keyxordecode(msg1,'Terminator X: Bring the noise'.encode()).decode('utf-8'))










