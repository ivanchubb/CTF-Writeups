question:
<pre>
Raj wanted to send a huge chunk of data. FInd it
Note : Enclose the flag in 'SHELL{' & '}'.
</pre>
files: COLD_COMPRESS.jpg

1) based on the name i'm immediately thinking a compressed file is inside
2) `binwalk -e COLD_COMPRESS.jpg`
<pre>
DECIMAL       HEXADECIMAL     DESCRIPTION
0             0x0             PNG image, 3840 x 2558, 8-bit/color RGBA, non-interlaced
17158270      0x105D07E       Zip archive data, at least v2.0 to extract, compressed size: 18722, uncompressed size: 48441, name: o.exe
17177027      0x10619C3       Zip archive data, at least v2.0 to extract, compressed size: 2987, uncompressed size: 17256, name: o
17180215      0x1062637       End of Zip archive, footer length: 22
</pre>

3) go into the extracted files `cd _COLD_COMPRESS.jpg.extracted/`
4) `ls -al`
<pre>
total 100
drwxr-xr-x 2 kali kali  4096 Jun  5 13:07 .
drwxr-xr-x 3 kali kali  4096 Jun  5 13:06 ..
-rw-r--r-- 1 kali kali 21967 Jun  5 13:06 105D07E.zip
-rw-r--r-- 1 kali kali 17256 May 22 20:09 o
-rw-r--r-- 1 kali kali 48441 May 22 20:11 o.exe
</pre>

5) strings o
6) gives us a lot of output, but the interesting pieces are "Hello World!" and "CRazy_MosQUIto_nEEDS_odoMOS"
**flag: CRazy_MosQUIto_nEEDS_odoMOS**