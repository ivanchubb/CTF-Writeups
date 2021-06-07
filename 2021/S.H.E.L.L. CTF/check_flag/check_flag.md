
question:
<pre>
Was cleaning the junk out of my PC, when I found this really old executable. Help me look for the flag.
</pre>
files: checkflag.exe

1) open the file in [ghidra](https://ghidra-sre.org/)
2) go to function "checkflag"
3) Decompiler display:
<pre>
ulonglong checkflag(int param_1)
{
  if (param_1 != 0x913) {
    printf("sorry try again.");
  }
  else {
    printf("Congrats you got it.");
    puts("\tThis is the flag");
    printf("SHELL{bas1c_r3v}");
  }
  return (ulonglong)(param_1 != 0x913);
}
</pre>

4) notice flag is SHELL{bas1c\_r3v}
**flag: SHELL{bas1c\_r3v}**