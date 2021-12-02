# MiniProject4-OS-

Team Members: Kofi Omari Asante and Stacy Nyamekye Sarfo


In this project, we are developing and deplying a web application using Docker. 
The web application must provide the following APIs:

/permissions?code=<number>
This API method accepts a code given by number and returns a JSON object specifying the permissions represented for owner, group and other. 
E.g., The request /permissions?code=744 should return 

{owner: [read, write, execute], group [read], other:[read]}.


/parity?b1=<bits>&b2=<bits>&b3=<bits>&b4=<bits>
This API method accepts the bits on corresponding disk blocks of a RAID-4 and returns the parity bits. Assume that each block has two bits. 
E.g., The request /parity?b1=00&b2=10&b3=11&b4=10 should return 11.

The goals of the project are to:
- Successfully deploy the web application using docker
- Create API methods created work correctly

