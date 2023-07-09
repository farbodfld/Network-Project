# Network-Project
At this project you can find two project about TCP and UDP protocol.

This repository contains two `calculator` and `P2PUDP` folders.

## Calculator Project
This project is about implementation of calculator witch you can ask the following opperations:
* Add
* Subtract
* Divide
* Multiply
* Sin
* Cos
* Tan
* Cot
The serve will responce to your equest and give you the answer and the calculation time.

## P2P-UDP Project
These softwares, perhaps one of the most famous of them is Torrent software, distribute files among users, and by not following the server and client model,
files are not distributed only from a certain number of points.

For simplicity, only the file distribution part is implemented, in this way, a software is implemented that has the ability to distribute a file or receive it,
in the mode of distributing the file by receiving the request using the UDP protocol for The requester sends and in the receiving state of the file,
it can generate an all-play request for that file.

for example :

`p2p - receive hello.txt`

With this command, the program is executed in the file receiving mode and the txt.hello file request is sent in the network as a broadcast to everyone.

For example, if one of the nodes is executed with the following command:

`p2p -server -filepaths c:\FileStore`

Upon receiving the request for the txt.hello file, it will send the response that is the desired file directly to the applicant.
Pay attention that the applicant must be listening on the same IP address and port with which he sent the request.

You should consider a specific port for the time when your software is distributing the file, and it will be your responsibility to choose this port.
Requesters can use random ports or a specific port.
Since the server responds based on the sent request, there is no difference between these two modes and it will be your responsibility to choose it.

Since UDP packets are limited, you need to consider a certain size for the packets and send the packets with that size,
if the file size is larger than the packet size, it should be sent piece by piece, finally on the side of the applicant it should be saved in a single file.

According to these explanations, for example, if we consider our packages to be 128 bytes and use the first byte to display the package number, we have.
For example, if the package number is equal to 10, it means that this package contains the tenth package of the sent file.

### How to run
To run this code you have two choice:

#### use the P2PUDP.py file
For run this code you should open two terminal and run the following command:
for run the server use `python P2PUDP.py -server "your/directory/path"` command and for run the client use `python P2PUDP.py -receive "filename.txt"` command.

