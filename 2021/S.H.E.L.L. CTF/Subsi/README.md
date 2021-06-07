
question:
<pre>
HITSS{5X65Z1ZXZ10F_E1LI3J}
</pre>
files: script.py
- based on the name we can assume it's a substitution cipher

looking at the script we get:
<pre>
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_1234567890'
key   = 'QWERTPOIUYASDFGLKJHZXCVMNB{}_1234567890'

text = <flag>

def encrypter(text,key):
    encrypted_msg = ''
    for i in text:
        index = alpha.index(i)
        encrypted_msg += key[index]
    # print(encrypted_msg)
    return encrypted_msg
</pre>

- looks like a 1 for 1 substitution using the included key.

1) copy paste the flag into a txt called flag
2) translate from key to alpha `cat flag | tr 'QWERTPOIUYASDFGLKJHZXCVMNB{}_1234567890' 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_1234567890'
`
- output:
<pre>
SHELL{5U65T1TUT10N_C1PH3R} 
</pre>
**flag: SHELL{5U65T1TUT10N_C1PH3R}**
