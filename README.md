# Remotely control your Zelio relay
Relay can be controlled from any computer running python in LOCAL NETWORK (not recommend using this on public networks because of security reasons). 

 ## About this project
This project is intended to hold relay closed until python program decides to stop it OR network has stopped functioning. If the relay can't communicate with the server zelio relay will release the output.

## If you want to run this you need:
1). Install python 3.6 (do not forget to add python to environment variables during installation).\
2). Run this command in your servers terminal: pip install pymodbus\
3). Change ip address of your zelio relay in main.py python program.\
4). Run main.py

## Any questions?
Leave a github issue or reach me via email.

## Zelio program

![Top](https://raw.githubusercontent.com/tomasvanagas/RemoteZelio/master/Top.png)
![Bottom](https://raw.githubusercontent.com/tomasvanagas/RemoteZelio/master/Bottom.png)
