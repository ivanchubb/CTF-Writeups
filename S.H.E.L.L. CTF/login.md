Question:
Sam really need to get past this login portal but isn't able too, can you help him? [http://3.142.122.1:8889/](http://3.142.122.1:8889/)

1) the link takes us to a login page
2) viewing page source we see a function called "main.js"
3) main.js checks for user "din_djarin11" and a password hash = "9ef71a8cd681a813cfd377817e9a08e5"
4) putting "9ef71a8cd681a813cfd377817e9a08e5" into [crackstation](https://crackstation.net/) gives result "ir0nm4n"
5) login with credentials: 'din_djarin11' and 'ir0nm4n' and you are given the flag
**flag: SHELL{th1s_i5_th3_wa7_845ad42f4480104b698c1e168d29b739}**