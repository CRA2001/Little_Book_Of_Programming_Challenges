'''
Write a program to perform a basic ‘Ceaser’ encryption and decryption on text.
This algorithm works by moving letters along by an
‘offset’. If the offset is 2 then b —> d, h—>j etc.
Try to write two functions—One called ‘encrypt’ and one called
’decrypt’. Both will return a string.
The user selects whether the wish to encrypt or decrypt.
The user enters sentence to encrypt and the encryption key (i.e.
How many we move the letters along—this is a smallish integer)
The program responds with the encrypted or decrypted version 
'''
def fun19_enc(text):
    text = list(text)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    enc = []
    # #enc_let = letters[letters.index(text.lower())+2]
    for i in range(0,len(text)):
        enc_let = letters[letters.index(text[i].lower())+2]
        enc.append(enc_let)
    return ''.join(enc)

def fun19_dec(text):
    text = list(text)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dec = []
    # #enc_let = letters[letters.index(text.lower())+2]
    for i in range(0,len(text)):
        dec_let = letters[letters.index(text[i].lower())-2]
        dec.append(dec_let)
    return ''.join(dec)

print(fun19_enc('Hi'))
print(fun19_dec(fun19_enc('Hi')))