## SFTP (secure file transfer protocol)

This protocol is used to transfer any type of files between two remote machines through their address on the network

### Steps
1. Establish a connection with remote machine
- Open your local terminal
- Run this command
~~~
local-machine$ sftp <user-name>@<ip-address>
~~~
> replace \<user-name> with actual remote machine username, and \<ip-address> with proper ip address	
> provide password of the remote machine if required	

2. Change the remote machine directory
- Run this commad
~~~
sftp> cd /path/to/directory/receiving/files
~~~
> replace \</path/to/directory/receiving/files> with the path that you want to recieve files you want to transfer there	

3. Using **put** command
- Run this command
~~~
sftp> put /path/to/file(s)
~~~
> replace \</path/to/file(s)> with the path to file or files existing on your local machine that you want to transfer to the remote	

4. Check remote machine
- Run this command
~~~
remote-machine$ cd /path/to/directory/receiving/files	
remote-machine$ ls
~~~
> check that files are properly transfered

5. Close the connection from local terminal
- You can end the connection by running this command
~~~
sftp> exit
~~~
or
~~~
sftp> quit
~~~
