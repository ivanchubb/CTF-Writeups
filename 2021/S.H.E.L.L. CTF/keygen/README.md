Question:
<pre>
Can you get the flag from the given file.
</pre>

files: [keygen.py](keygen.py)

read file in notepad:
<pre>
def checkends(password):
    end_status = 0
    if password[:6] == "SHELL{":
        end_status = 1
    if password[28] == "}":
        end_status = 1
    return end_status
def checkmiddle1(password):
    middle1_status = 0
    if password[27] == "1"  and password[17] == "4" and password[8] == "n" and password[23] == "y" and password[10] == "0":
        middle1_status = 1
    if password[11] == "n" and password[12] == "z" and password[13] == "a" and password[21] == "g" and password[15] == "u":
        middle1_status = 1
    if password[16] == "r"and password[7] == "3" :
        middle1_status = 1
    return middle1_status
def checkmiddle2(password):
    middle2_status = 0
    if password[18] == "_" and password[25] == "5" and password[20] == "4" and password[14] == "k" and password[22] == "3" and password[9] == "b"  and password[24] ==  "0":
        middle2_status = 1
    if  password[19] == "k" and password[26] == "h" and password[6] == "s" :
        middle2_status = 1
    return middle2_status
# driver code

a = input("enter your flag:")
if checkends(a) == 1 and checkmiddle1(a) == 1 and checkmiddle2(a) == 1:
    print("congrats thats the flag.")
else:
    print("Wrong flag.")
</pre>

looks like it takes the password as an array and then checks all the indices for their values.

1) starting from password[6] and working our way to password[27] we get:


**flag: SHELL{s3nb0nzakur4_k4g3y05h1}**
