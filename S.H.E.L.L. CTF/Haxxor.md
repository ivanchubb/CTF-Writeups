Question:

<pre>
Encrypted string : 0x2-0x19-0x14-0x1d-0x1d-0x2a-0x9-0x61-0x3-0x62-0x15-0xe-0x60-0x5-0xe-0x19-0x4-0x19-0x2c
</pre>

1) looks like we are given a string of hexidecimals.  The question doesn't specify that the flag is in a format different form the standard "SHELL{}".  Additionally, we see "0x1d" is the 4th and 5th characters. assuming those map to "LL", then the key probably doesn't change per position
2) it's not a ROT cipher because you get very inconsistent results with that, some characters make sense, others don't. for example to make the first character "0x2" = the first known character in ASCII "S" you need to increase by 0x51. when you do that with 0x19 you get different results.  
3) looking at the name of the challenge "HAXXOR" made me think to XOR the numbers with 0x51. When i did i got the flag
4) **flag: SHELL{X0R3D\_1T\_HUH}**

BONUS:

This can also be solved with [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')To_Hex('Space',0)Magic(3,true,true,'SHELL')&input=MDIgMTkgMTQgMWQgMWQgMmEgMDkgNjEgMDMgNjIgMTUgMGUgNjAgMDUgMGUgMTkgMDQgMTkgMmMK)
with input: 02 19 14 1d 1d 2a 09 61 03 62 15 0e 60 05 0e 19 04 19 2c
and recipes
1) from HEX
2) To HEX
3) Magic (with intensive mode, extensive language support, and Crib = SHELL)
