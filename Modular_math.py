#!/usr/bin/python3

import json
from pwn import *
import binascii
import base64
from Crypto.Util.number import long_to_bytes


# given x and p if there is a number a such that (a**2)%p = x.
# then x has a quadratic residue for the values a.
# if not, then the integer is a quadratic non-residue

#this method works with small values p
nums = [14,6,11,18]
p = 29
for i in nums:
    for j in range(p):
        if (j**2)%p ==i:
            print("answer is:",j, "for a=",i)
# 6 has a quadratic residue mod 29 with values 8 and 21
# these values (6 and 8) are called the square root modulo of 6
# modulo p square root a; a = (x**2)%p

# quadratic residue **2 = quadratic residue
# quadratic residue * non-quadratic residue = non-quadratic residue
# quadratic non-residue *quadratic non-residue = quadratic residue

# legendre is a faster way to check if a quadratic residue exists
# Legendre symbol is (a**((p-1)/2))%p.
# if this equal 1 (a is quadratic residue)
# if this equal -1 (a is a quadratic non-residue)
# if this equal 0 (a%p =0)
