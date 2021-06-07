
URL: [http://3.142.122.1:8885/](http://3.142.122.1:8885/)

page displays:
<pre>
This web app is still under development
</pre>

1) viewing the source code we see comment
<pre>
TODO: Develop auth, buy some cookies from the supermarket
</pre>

2) lets look at our cookies

We have a cookie named "privilege" with value "dXNlcg%3D%3D"

3) googling this shows that it is base64 for "user"
4)  lets change it to base64 for "admin"
[using base64encode.org](https://www.base64encode.org) we input admin and get:
<pre>
YWRtaW4=
</pre>
5) "=" is %3D so change our user value to our new admin value of "YWRtaW4%3D"
6) Refresh the page and we have our flag!
**flag: SHELL{0NLY\_0R30\_8e1a91a632ecaf2dd6026c943eb3ed1e}**