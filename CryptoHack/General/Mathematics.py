from Crypto.Util.number import *
from pwn import *
import binascii
import base64
from PIL import Image, ImageChops
from math import gcd
# coprime is when GCD of 2 nums is 1
# Euclids Algorithm can calc GCD of 2 ints
a= 66528
b= 52920

def mygcd(a, b):
    # edge case
    if a%b ==0:
        return b
    a1 = a
    b1 = b
    tmp = []
    remainder = []
    while True:
        tmp.append(a1//b1)
        remainder.append(a1%b1)
        a1 = b1
        b1 = remainder[-1]
        if b1 ==0:
            break
    tmp.pop()
    remainder.pop()
    return remainder[-1]


# Python program for the extended Euclidean algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x


gcd,x,y = egcd(26513,32321)
print("The GCD is", gcd)
print(f"x = {x}, y = {y}")

#print(8146798528947%17)

print((3**17)%17)

# fermats little theroem is any number a to power x mod x = a (a**x%x=a)
# any number a to power x mod x+1 = 1
# a**(p-1)%p=1
# a**(p-2)%p=a**-1
print((3**11)%13)
#
