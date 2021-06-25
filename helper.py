import base64

#converts hex to bytes
def hextobytes(val):
    return bytes.fromhex(val)

#converts bytes to base64
def bytestobase64(val):
    return base64.b64encode(val)

#converts base64 to bytes
def base64tobytes(val):
    return base64.b64decode(val)


#Does the XOR operation between bytes of equal length
def fixedxor(byte1,byte2):
    bytefinal=[1]*(len(byte1))
    for i in range(0,len(bytefinal)):
        bytefinal[i]=byte1[i]^byte2[i]
    return bytes(bytefinal)
    

#Does the XOR operation of a byte with another single byte
def singlebytexor(byte1,byte2):
    bytefinal=[1]*(len(byte1))
    for i in range(0,len(bytefinal)):
        bytefinal[i]=byte1[i]^byte2[0]
    return bytes(bytefinal)



#Encode the plaintext with key
def keyxor(byte1,kbyte):
    #making the byte key length equal to the length of byte message
    i=0
    j=0
    lkey=bytes()
    while i<len(byte1):
        if j>=len(kbyte):
            j=0
        lkey+=chr(kbyte[j]).encode()
        j+=1
        i+=1
    
    return fixedxor(byte1,lkey)



#Decode the ciphertext with key
def keyxordecode(byte1,kbyte):
    return keyxor(byte1,kbyte)
    

    


#returns the int value of the single key xored for creating ciphertext
def bruteforcechrs(bt):
    allbtxored=[]
    for i in range(255):
        btxored=bytes()
        for j in range(len(bt)):
            btxored+=chr(bt[j]^i).encode()
        allbtxored.append(btxored)

    frequencytable={ 'a' :  8.167,  'b' : 1.492, 'c' : 2.782, 'd' : 4.253,
                'e' : 12.702,  'f' : 2.228, 'g' : 2.015, 'h' : 6.094,
                'i' :  6.966,  'j' : 0.153, 'k' : 0.772, 'l' : 4.025,
                'm' :  2.406,  'n' : 6.749, 'o' : 7.507, 'p' : 1.929,
                'q' :  0.095,  'r' : 5.987, 's' : 6.327, 't' : 9.056,
                'u' :  2.758,  'v' : 0.978, 'w' : 2.360, 'x' : 0.150,
                'y' :  1.974,  'z' : 0.074, ' ' : 15 }
    
    byteval=0
    frequencies=[]
    for btxored in allbtxored:
        
        frequencycount=0
        for i in range(len(btxored)):
            if chr(btxored[i]) in frequencytable.keys():
                frequencycount+=frequencytable[chr(btxored[i])]
        frequencies.append((byteval,round(frequencycount,3)))
        byteval+=1

    highfrequency=0
    highfrequencyint=0

    for i in range(len(frequencies)):
        if frequencies[i][1] >highfrequency:
            highfrequencyint=frequencies[i][0]
            highfrequency=frequencies[i][1]
    
    return highfrequencyint



#function that returns Hamming distance between two strings
def hammingdis(bytemsg1,bytemsg2):


    #doing the xor operation between 2 bytes
    result=fixedxor(bytemsg1,bytemsg2)

    #converting the resultant byte after xor operation to binary
    bytebin=bin(int(result.hex(),16))[2:]


    #counting the number of ones in the binary
    count=0

    for i in range(0,len(bytebin)):
        if bytebin[i]=='1':
            count+=1

    return count




# #calcute character frequency in a byte and return bytes value of characters with highest frequency
# def charfreq(val):
#     #dictonary to map char int value with its frequency
#     bytedict={}


#     for i in range(0,len(val)):
#         if val[i] not in bytedict:
#             bytedict[val[i]]=1
#         else:
#             bytedict[val[i]]+=1



#     #finding the characters with the highest frequencies
#     freq=0
#     guess=[]
#     for i in bytedict.keys():
#         if(bytedict[i]>freq):
#             guess=[]
#             guess.append(i)
#             freq=bytedict[i]
#         elif(bytedict[i]==freq):
#             guess.append(i)
        

#     retbytes=[]

#     #returns the byte value of all the characters with high occurence frequencies

#     for i in guess:
#         if i>15:
#             retbytes.append(bytes.fromhex(hex(i)[2:]))
#         else:
#             hexval=hex(i)[2:]
#             temp='0'
#             retbytes.append(bytes.fromhex(temp+hexval))
    
#     return retbytes

        
    


            
