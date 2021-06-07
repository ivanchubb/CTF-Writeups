Question:

Can you help me decrypt? UYCAE{J0\_P0A\_CFE\_XF335}

1) looks like it's still in the SHELL{} format. and based on the underscores i don't think any letters have changed positions.  We also don't know it's a ROT shift because if so, the 'LL' in "SHELL" would have the same letters
2) googling poly-alpha gives some cringe social media site, but also "poly-alphabetic" ciphers. specifically vigniere
3) using [dcode.fr](https://www.dcode.fr/vigenere-cipher) and known plaintext of "SHELL{" gives you the partial key of "CRYPT" [image](dcode.png)
4) This was the sticking point for me for awhile,  then i realized that you can't have numbers in the key for a vigneire cipher and therefore the numbers in the flag won't change posistionsusing [cyber chef](https://gchq.github.io/CyberChef/) and a [vigniere square](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#/media/File:Vigen%C3%A8re_square_shading.svg) 
6) since the start of the key is "crypt" i try variations of it and land on "cryptochallenge"
7) the flag is now SHELL{V0_N0T_CUT_TS335}
8) i can change the V to an D by making the 6th letter in the key a "g" 
9) assuming the last word is "trees" [not many 5 letter words end in ees](https://www.thefreedictionary.com/words-that-end-in-ees) we change the last letter in the key to "o". 
10) Now our key is "cryptgchalleo" and the 

13) **flag is SHELL{D0_N0T_CUT_TR335}**
