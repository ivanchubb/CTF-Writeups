![Question](Screenshot_3.png)
1) Visiting the page gives us:
![page](Screenshot_2.png)
2) The text mentions using a special browser.  Websites know what browser or [user agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) you are using based on your get request to the page.
3) we can change that user agent value using [burpsuite](https://portswigger.net/burp)
![burp](Screenshot_5.png)
4) And we get the flag! ![flag](Screenshot_1.png)
5) flag: **bcactf{y0u_h@ck3d_5tegos@urus_1nt3lligence}**