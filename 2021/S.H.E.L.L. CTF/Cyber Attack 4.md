Quesstion: 
We have top secret confidential information from the secret service that there is going to be an all out cyber attack against a country in the future. Long Live our spy who died in between the transmission.

The FBI have found that the following tools will be used in attack on the country.Use this GitHub repo as a starting point for your investigation [https://github.com/norias-teind/tools](https://github.com/norias-teind/tools) All we ask from you is : The Country of Attack

1) I racked my head against this one for the better part of a day and tried a lot of failed approaches.  Eventually i just gave up and brute forced it using Burpsuite's intruder on sniper mode
2) intercept the POST request and send it to intruder
3) clear all positions and change the bottom line to `{"challenge_id":31,"submission":"SHELL{§§}"}`
4) set payload as [list of all countries](https://gist.github.com/kalinchernev/486393efcca01623b18d)
5) "start attack"
6)  you get rate limited pretty quickly so, just remove names you already have checked. Eventually you get a hit with "Netherlands"
**flag: SHELL{Netherlands}**
