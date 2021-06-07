question:
<pre>
Raj wanted to send a msg to Brad but he wanted to hide it from his wife? Can you help Brad decode it?
Note : Wrap the flag in 'SHELL{' & '}'.
</pre>
files: mystic-fairy-girl-magical-dark-sgi-3840x2558-5287.jpg

1) i noticed that the format is in .jpg but the file is a .png, but that didn't change anything.  tried running strings, xxd, and exiftool to look for some obvious answers, but didn't get anywhere
2) popped it into [stegsolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install) and looked through different filters, but didn't get anywhere there either
3) Went 1 by 1 through all of [cyberchef](https://gchq.github.io/CyberChef/) tools and when i got to "Extract LSB"  using default values it produced the string "NarUTO_Is_hokaGE"

**flag: SHELL{NarUTO_Is_hokaGE}**
