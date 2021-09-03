#!/bin/python3

import json
from pwn import *
import binascii
import base64
from Crypto.Util.number import long_to_bytes

# ASCIIs
ASCIIs = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
chrs = ""
for i in ASCIIs:
    chrs +=  chr(i)
print(chrs)

#HEX
hexvals = b'63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

print(binascii.a2b_hex(hexvals))

#Base64
temp = bytes.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')
print(base64.b64encode(temp))

#Bytes and big numbers
given = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(given))
