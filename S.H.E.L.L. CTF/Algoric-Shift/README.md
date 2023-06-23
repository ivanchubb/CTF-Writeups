Question:
<pre>ciphered text : HESL{LRAT5PN51010T_CNPH1R}3

Try decrypting:
</pre>

files: [script.py](script.py)
<pre>
text = 'flag{...}'

key = [3,1,2]

li0 = []
li1 = []
li2 = []
for i in range(0,len(text)):
    if i % 3 == 0:
        li0.append(text[i])
    elif (i - 1) % 3 == 0:
        li1.append(text[i])
    elif (i - 2) % 3 == 0:
        li2.append(text[i])
li = []
for i in range(len(li1)): 
    li.append(li1[i]) 
    li.append(li2[i])
    li.append(li0[i])

# print(li)
print("The ciphered text is :")
ciphered_txt = (''.join(li))
print(ciphered_txt)
</pre>

- looks like another substitution cihper, this time changing the shift based on the key and then appending them in  order of %1, %2, %0
- also looks like the key is listed as "3, 1, 2"
1) to reverse it:
2) lets just open the script and change the for loop to be 
``` for i in range(len(li1)): 
    li.append(li2[i]) 
    li.append(li0[i])
    li.append(li1[i])
```
and
`text = HESL{LRAT5PN51010T_CNPH1R}3`
3) run script.py
<pre>
The ciphered text is :
SHELL{TRAN5P051T10N_C1PH3R}
</pre>
**flag: SHELL{TRAN5P051T10N_C1PH3R}**
