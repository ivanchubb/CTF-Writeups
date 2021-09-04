from Crypto.Util.number import *
from pwn import *
import binascii
import base64
from PIL import Image, ImageChops
from math import gcd
# coprime is when GCD of 2 nums is 1
# Euclids Algorithm can calc GCD of 2 ints
a= 66528
b=52920
print(gcd(a,b))
