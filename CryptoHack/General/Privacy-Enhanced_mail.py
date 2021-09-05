from Crypto.Util.number import *
from pwn import *
import binascii
import base64
from PIL import Image, ImageChops
from math import gcd


# openssl pkey -in pem.pem -text
input = "7c:3b:1d:53:4f:29:9b:43:c1:26:08:76:30:3c:0a:95:be:17:bf:91:a5:df:2f:1c:ac:da:7c:75:a0:23:6e:4f:81:e1:21:0d:27:c0:12:6f:b3:4d:80:f2:7a:41:a4:d7:e4:8c:a7:c5:b0:e7:88:78:b1:9f:d0:d6:c0:bf:68:30:fb:8a:44:01:b1:6d:93:8a:d5:4c:4d:0b:35:68:62:05:6c:b0:55:4e:b2:ab:83:90:ad:18:25:b3:1d:af:bf:2f:c0:5d:19:4f:38:c2:f2:24:20:d3:21:0a:da:02:30:24:26:40:ca:e0:05:eb:85:cb:c8:dc:ca:18:25:ea:74:96:d9:b1:70:c5:cb:fe:35:4f:e1:9a:63:10:2b:82:f3:8d:5d:7c:25:17:35:20:8b:83:a5:42:40:92:7f:89:98:48:c1:6a:5f:e7:0c:e9:50:da:ff:7b:f9:f4:b7:1b:59:81:01:a5:20:48:cd:30:c1:6c:b9:94:33:0b:10:59:2d:2c:95:d4:d0:e5:79:f5:28:7f:f7:4a:88:26:8d:03:89:69:8c:8f:7b:9a:e8:13:f3:92:46:89:3d:02:66:1c:f0:8d:9c:bc:ec:9f:72:2c:f7:6d:0e:96:f1:e1:77:37:e2:9e:ce:86:76:76:7c:b6:e1:df:0d:bd:2d:73:1e:d8:48:b1"
key = "0x" +"".join(input.split(":"))
print(int(key,16))

# openssl x509 -inform der -in 2048der.der -text
input = "00:b4:cf:d1:5e:33:29:ec:0b:cf:ae:76:f5:fe:2d:c8:99:c6:78:79:b9:18:f8:0b:d4:ba:b4:d7:9e:02:52:06:09:f4:18:93:4c:d4:70:d1:42:a0:29:13:92:73:50:77:f6:04:89:ac:03:2c:d6:f1:06:ab:ad:6c:c0:d9:d5:a6:ab:ca:cd:5a:d2:56:26:51:e5:4b:08:8a:af:cc:19:0f:25:34:90:b0:2a:29:41:0f:55:f1:6b:93:db:9d:b3:cc:dc:ec:eb:c7:55:18:d7:42:25:de:49:35:14:32:92:9c:1e:c6:69:e3:3c:fb:f4:9a:f8:fb:8b:c5:e0:1b:7e:fd:4f:25:ba:3f:e5:96:57:9a:24:79:49:17:27:d7:89:4b:6a:2e:0d:87:51:d9:23:3d:06:85:56:f8:58:31:0e:ee:81:99:78:68:cd:6e:44:7e:c9:da:8c:5a:7b:1c:bf:24:40:29:48:d1:03:9c:ef:dc:ae:2a:5d:f8:f7:6a:c7:e9:bc:c5:b0:59:f6:95:fc:16:cb:d8:9c:ed:c3:fc:12:90:93:78:5a:75:b4:56:83:fa:fc:41:84:f6:64:79:34:35:1c:ac:7a:85:0e:73:78:72:01:e7:24:89:25:9e:da:7f:65:bc:af:87:93:19:8c:db:75:15:b6:e0:30:c7:08:f8:59"

key2 = "0x" + "".join(input.split(":"))
print(int(key2,16))

#ssh-keygen -e -f <(cat path/to/key ) -m PKCS8 > foo.pub
#openssl rsa -inform PEM -pubin -in foo.pub -text -noout
modulus = "00:ad:3c:ba:9b:6b:e1:85:bc:31:dd:15:5b:35:56:f7:64:e7:a7:0a:aa:ac:39:71:da:26:96:ed:37:e3:ae:ba:52:ca:05:22:a9:22:83:c1:f9:90:db:0d:79:f4:a9:69:1f:e2:53:b1:b4:64:a0:a2:59:14:6e:01:b4:ec:b8:73:7e:0b:3e:76:e9:78:50:bf:38:0a:4c:19:13:19:85:dd:17:f5:9d:1b:fe:bf:ba:6a:2e:dd:9d:3e:c0:9b:d3:66:0b:c4:99:e1:1c:96:f8:ad:06:b3:d9:93:38:40:2b:53:39:ca:98:0d:47:8a:7c:b1:c2:69:95:38:12:49:bf:38:0a:4a:ae:97:f0:e3:fd:28:7e:7f:0a:3a:b1:4d:d2:de:3f:76:a9:cd:bb:05:51:82:86:94:22:1b:08:e3:ba:de:02:90:76:ae:cd:00:3f:80:a0:81:22:22:f2:ce:81:5c:2c:41:e1:8c:e0:4e:10:4a:e7:be:b4:4f:58:22:00:26:10:0b:93:05:76:ad:46:c3:e2:0d:48:59:ae:d0:23:6a:b7:9c:1d:27:96:78:cf:9e:38:f0:69:1e:d3:a4:7e:20:cb:63:52:21:83:43:74:2d:4f:67:ca:de:05:a1:67:19:35:e0:ce:14:36:b7:44:4e:04:d6:fe:64:38:07:f0:5c:be:29:31:be:80:46:a4:a6:ed:b4:6d:1a:81:f3:a3:4d:e9:fa:c3:2c:e9:19:f7:1d:f0:df:6b:49:b6:aa:ab:25:30:0b:cb:83:a2:dc:c5:b4:5c:f3:ba:d5:40:53:d7:7d:d5:36:a0:1b:35:81:84:da:0c:7e:99:70:55:39:ec:db:b1:8e:3a:0b:f5:76:7e:6c:41:24:92:98:fd:21:4d:b3:cc:0e:54:e1:ca:c2:a4:47:d0:62:39:56:c1:b5:61:90:a5:5f:77:ea:93:c1:83:25:84:44:6a:8c:a8:2f:71:ca:42:dd:54:7b:f6:56:ed:39:4f:45:8c:c0:a0:80:7a:d8:2d"

key3 = "0x" + "".join(modulus.split(":"))
print(int(key3,16))
