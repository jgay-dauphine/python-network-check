import socket
from os import system as system_call
from os import devnull
from platform import system as system_name
from subprocess import check_output
from xml.etree.ElementTree import fromstring


def ping(host):
    """returns True if the host (str) respond to ping, False otherwise"""
    params = "-n 1 -w 2 " if system_name().lower() == "windows" else "-c 1 -w 2 "
    redirect = " > " + devnull
    return system_call("ping " + params + host + redirect ) == 0

def getNics() :

    cmd = 'wmic.exe nicconfig where "IPEnabled  = True" get ipaddress,DNSHostName,DefaultIPGateway /format:rawxml'
    xml_text = check_output(cmd, creationflags=8)
    xml_root = fromstring(xml_text)

    nics = []
    keyslookup = {
        'DNSHostName' : 'hostname',
        'IPAddress' : 'ip',
        'DefaultIPGateway' : 'gateway',
    }

    for nic in xml_root.findall("./RESULTS/CIM/INSTANCE") :
        # parse and store nic info
        n = {
            'hostname':'',
            'ip':[],
            'gateway':[],
        }
        for prop in nic :
            name = keyslookup[prop.attrib['NAME']]
            if prop.tag == 'PROPERTY':
                if len(prop):
                    for v in prop:
                        n[name] = v.text
            elif prop.tag == 'PROPERTY.ARRAY':
                for v in prop.findall("./VALUE.ARRAY/VALUE") :
                    n[name].append(v.text)
        nics.append(n)

    return nics

def getGateway():
    nics = getNics()
    gw = nics[0]["gateway"][0]
    return gw

def nslookup(name):
    try:
        socket.gethostbyname(name)
    except socket.gaierror, err:
        print "cannot resolve hostname: ", name, err
        return False
    return True

# Protocole de test reseaux :
if ping("127.0.0.1"):
    print "Ping 127.0.0.1 ... OK"
else:
    print "Ping 127.0.0.1 ... NOK ==> Stop du test"
    exit()

# Ping passerelle
gw = getGateway()
if ping(gw):
    print "Ping Gateway (" +gw+ ") ... OK"
else:
    print "Ping Gateway (" +gw+ ") ... NOK => Stop du test"
    exit()

# Ping 8.8.8.8
if ping("8.8.8.8"):
    print "Ping 8.8.8.8 ... OK"
else:
    print "Ping 8.8.8.8 ... NOK ==> Stop du test"
    exit()

# Ping IP particuliere
ip = '192.168.0.1'
if ip and not ip == '':
    if ping(ip):
        print "Ping", ip, " ... OK"
    else:
        print "Ping", ip,  " ... OK ==> Stop du test"
        exit()

# nslookup google
name = "www.google.com"
if nslookup(name):
    print "Nslookup", name, "... OK"
else:
    print "Nslookup", name, "... NOK ==> Stop du test"
    exit()

# nslookup site
name = "www.google.com"
if nslookup(name):
    print "Nslookup", name, "... OK"
else:
    print "Nslookup", name, "... NOK ==> Stop du test"
    exit()

system_call("PAUSE" if system_name().lower() == "windows" else "pause")