
Question:
http://3.142.122.1:9335/

page displays:
```
# Make sha256 collide and you shall be rewarded
**The source!**
<html>  
    <body>  
        <h1> Make sha256 collide and you shall be rewarded </h1>  
  
        <b>The source!</b>  
  
        <?php  
            $source = show_source("index.php", true);  
            echo("<div>");  
            print $source;  
            echo("</div>");  
  
            if (isset($_GET['shell']) && isset($_GET['pwn'])) {  
                if ($_GET['shell'] !== $_GET['pwn'] && hash("sha256", $_GET['shell']) === hash("sha256", $_GET['pwn'])) {  
                    include("flag.php");  
                    echo("<h1>$flag</h1>");  
                } else {  
                    echo("<h1>Try harder!</h1>");  
                }  
            } else {  
                echo("<h1>Collisions are fun to see</h1>");  
            } ?>  
    </body>  
</html>`
# Collisions are fun to see
```

1) looks like we need to make a sha256 collision using the variables 'shell' & 'pwn' on url/index.php.
2) setting values nothing with http://3.142.122.1:9335/index.php?shell&pwn returns "Try Harder!"
3) feeding them values as both 0 returns the same "Try Harder!" message.
4) googling around i saw a [workaround on stack overflow](https://stackoverflow.com/questions/53080807/sha256-hash-collisions-between-two-strings/53081240)
5) basically assign the values of shell and pwn as arrays to break the hashing algorithm
6) http://3.142.122.1:9335/index.php?shell[0]=0&pwn[1]=0
**flag: SHELL{1nj3ct\_&\_coll1d3\_9d25f1cfdeb38a404b6e8584bec7a319}**