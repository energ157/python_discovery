from PowerShell import *
from NetworkFunctions import *
from Menu import takeChoiceAdapter, takeChoiceAPIPA, takeChoicePorts
import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor

def detectAdaptersAndDiscover(PortChoice):
    Adapters = calculateAdapters()
    choice = takeChoiceAdapter(Adapters)
    if choice == 999:
        Discover(list(Adapters.values()),PortChoice) #All Adapters Option
    else:
        Discover(Adapters[choice],PortChoice)
        
    
    
    
    

def Discover(Adapters,PortChoice):
    if PortChoice == 2:
        Ports = takeChoicePorts()
    for Adapter in Adapters:
        ip = calculateIP(Adapter)
        subnetMask = calculateSubnet(Adapter)
        print(Adapter)
        print("Assigned IP:", ip)
        if ip[:7] == "169.254":
            choice = takeChoiceAPIPA(Adapter)
            if choice == 2:
                ICMPBasedHostDetection(ip, subnetMask, Ports)
                
        else:
            ICMPBasedHostDetection(ip, subnetMask, Ports)
        print("===========================")
        print()
    

    


def ICMPBasedHostDetection(ip, subnet, Ports=[]):
    ip = ip.strip()
    subnet = subnet.strip()
    network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
    with ThreadPoolExecutor(max_workers=100) as executor:
        for host in network:
            executor.submit(checkIP,host,Ports)


def checkIP(addr,Ports):
    addresses = []
    command = f'(Test-Connection "{addr}" -Count 1 -Quiet)'
    check = Powershell_execution(command)
    if 'True' in check:
        print(addr, "is up!\n")
        if len(Ports) > 0:
            with ThreadPoolExecutor(max_workers=100) as executor:
                for port in Ports:
                    executor.submit(checkTCPport,str(addr),port)

def checkTCPport(addr,port, timeout=0.2):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    result = sock.connect_ex((addr, port))
    sock.close()

    if result == 0:
        print(addr + ':', "Port",port,"is open!")
    else:
        print(addr + ':', "Port",port,"is closed.\n")

