#!/bin/python3

import json
from pwn import *
import binascii
import base64
from Crypto.Util.number import *


conn = remote("socket.cryptohack.org", 13377)
j= 0
while j<105:
    dict =json.loads(conn.recv())
    if "flag" in dict:
        print("flag is ",dict["flag"])
        break
    #print(dict)
    if dict["type"] == "hex":
        #print(binascii.a2b_hex(dict["encoded"]))
        #print(dict["type"])
        #print(binascii.a2b_hex(dict["encoded"]))
        ans = {"decoded" : binascii.a2b_hex(dict["encoded"]).decode("utf-8")}
        conn.send(json.dumps(ans))

    elif dict["type"] == "rot13":
        #print(dict["type"])
        #print(dict["encoded"])
        tmp = ""
        for i in dict["encoded"]:
            if (ord(i))<97:
                tmp += i
                continue
            tmp += chr((ord(i)-97+13)%26+97)
        #print(tmp)
        ans = {"decoded":tmp}
        conn.send(json.dumps(ans))

    elif dict["type"] == "base64":
        #print(dict["type"])
        #print(dict["encoded"])
        tmp = base64.b64decode(dict["encoded"])
        ans = {"decoded" : tmp.decode("utf-8")}
        conn.send(json.dumps(ans))

    elif dict["type"] == "utf-8":
        #print(dict["type"])
        temp = ""
        for i in dict["encoded"]:
            temp += chr(i)
        #print(temp)
        ans = {"decoded" : temp}
        conn.send(json.dumps(ans))

    elif dict["type"] == "bigint":
        #print("bigint")
        binascii.a2b_hex(dict["encoded"][2:])
        tmp = binascii.a2b_hex(dict["encoded"][2:])
        ans = {"decoded" : tmp.decode("utf-8")}
        conn.send(json.dumps(ans))
    j+=1
    print(j)
