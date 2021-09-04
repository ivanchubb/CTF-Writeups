from Crypto.Util.number import *
from pwn import *
import binascii
import base64
from PIL import Image, ImageChops

word = "label"
answer =""
for i in word:
    answer+= chr(ord(i)^13)
print("crpyto{",answer,"}")

# A ^ B = B ^ A
# A ^ (B ^ C) = (A ^ B) ^ C
# A ^ 0 = A
# A ^ A = 0

'''
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
'''
# binascii.a2b_hex will convert the byte string to bytehex so it will xor with hex vals instead of with ascii vals
key1 = binascii.a2b_hex(b'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
#print(key1)
key2 = xor(key1, binascii.a2b_hex(b'37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'))
#print(key2)
key3 = xor(key2, binascii.a2b_hex(b'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'))
#print(key3)
flag = xor(xor(xor(binascii.a2b_hex(b'04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'),key3),key2),key1)
print(flag)

given = b'73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
givenb = binascii.a2b_hex(given)
#print(givenb)
key = xor('c','s')
print(xor(givenb,key))

given = b'0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
givenb = binascii.a2b_hex(given)
#got "crypto{" from the flag type, and brute forced the last char
key = xor(givenb,b'crypto{1')[:8]
print(xor(key,givenb))

im1 = Image.open(r"CryptoHack\General\flag.png")
im2 = Image.open(r"CryptoHack\General\lemur.png")
im3 = ImageChops.subtract(im2,im1)
im3.show()
