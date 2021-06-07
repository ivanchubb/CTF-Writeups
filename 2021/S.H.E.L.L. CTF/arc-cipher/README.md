Question:

cipher\_text : a7 f9 de 54 29 92 7f 61 9a 7a 5f f3 f4 1a 88 a1 8f ca 97 47
files: [script.py](script(4).py)

1) looking at script.py we are luckily given the key "MANGEKYOU"
2) the program creates a new key by converting the current one to hex and does some encryption using a XOR. with this information we can solve it.
3) to make things easier i added a `print("new key is ", key_new)` below the function "key_new" and then i changed the input text to various lengths with different characters.  turns out that the new key doesn't change values, only changes length with the size of the input text.
4) set the input text to a length greter or equal to the cipher text in the question (20 characters) and you get the following new key
<pre>[244, 177, 155, 24, 101, 233, 44, 85, 201, 49, 10, 192, 171, 79, 203, 233, 190, 130, 163, 58, 215, 68, 35, 123, 48, 54, 196, 147, 42, 250]
</pre>
5) Then XOR each of these numbers (in hex) with the respective index in the key to get the flag. this can be done in [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Decimal','string':'244'%7D,'Standard',false)&input=YTc) to speed things up. Someone smarter than me could have probably automated it too, but i just did each piece individually.
6) **flag: SHELL{S4SKU3_UCH1H4}**
