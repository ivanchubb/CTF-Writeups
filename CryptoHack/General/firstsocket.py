#!/usr/bin/env python3

import telnetlib
import json
from pwn import *

conn = remote("socket.cryptohack.org", 11112)

data = conn.recvS()
print(data)

request = {
    "buy": "flag"
}
conn.send(json.dumps(request).encode())
flag = conn.recvS()
print(json.loads(flag))
conn.close()
