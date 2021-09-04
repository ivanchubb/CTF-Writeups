from Crypto.Util.number import *
from pwn import *
import binascii
import base64
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
key1 = b'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'.hex()
print(key1)
key2 = xor((b'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'.hex()),b'37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'.hex())
key3 = xor(key2,b'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'.hex())
flag = xor(xor(xor(b'04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'.hex(),key3),key2),key1)
#print(binascii.b2a_hex(flag))
#print((bytes_to_long(flag).decode("utf-8")))
print(long_to_bytes(flag))
