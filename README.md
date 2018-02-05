# python-network-check

A small tool to test network when a user says "The Internet is not working, fix it"

## Concept

This script test the following things :
* ping 127.0.0.1
* ping gateway
* ping 8.8.8.8
* ping special IP (need configuration inside)
* nslookup www.google.fr
* nslookup special website (need configuration inside)

## Example of output
Ping 127.0.0.1 ... OK
Ping Gateway (192.168.0.1) ... OK
Ping 8.8.8.8 ... OK
Ping 192.168.0.1  ... OK
Nslookup www.google.com ... OK
Nslookup www.google.com ... OK
Appuyez sur une touche pour continuer...

## Installation

For the integration to work out of the box you should have the following prerequisites :
* a valid python interpretor in c:\Python27\python.exe
* the networkTester.py file deployed in c:\Python27\Scripts\

Once this is done, juste run the reg_windows10.reg file so you can use the contextual menu integration easily

## Content of the reg file

For the sake of anyone asking what this reg file is doing here is the whole thing. In short this ONLY add a "Tester le réseau" (french for "test network") entry in the contextual menu when opened in the background of a directory (your desktop for short).

If you whish you can override here the location of your python installation

~~~
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\NetworkCheck]
@="Tester le réseau"

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\NetworkCheck\command]
@="c:\\python27\\python.exe c:\\Python27\\Scripts\\networkTester.py"
~~~

## Disclamer

This script is given as is, and no blame could be send for whatever you use it for. It was build for one purpose at work and will not be updated if I don't really need it. You can try and ask for some things but don't expect a positive answer everytime. This was tested on Windows 10 system and should work on Windows, Mac and Linux, but is not tested as of today.

Have fun and code more !