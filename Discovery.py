from PowerShell import *
from NetworkFunctions import *

def detectAdaptersAndDiscover():
    Adapters = calculateAdapters()
    
    

def Discover(Adapters):
    Adapters = calculateAdapters()
    for Adapter in Adapters:
        ip = calculateIP(Adapter)
        subnetMask = calculateSubnet(Adapter)
        print(Adapter)
        print("Assigned IP:", ip)
        if ip[:7] == "169.254":
            print("APIPA address detected, skipping")
        else:
            ICMPBasedHostDetection(ip, subnetMask)
        print("===========================")
        print()
    

    


def ICMPBasedHostDetection(ip, subnet):
    ip = ip.strip()
    subnet = subnet.strip()
    network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(checkIP,network)

def checkIP(addr):
    addresses = []
    command = f'(Test-Connection "{addr}" -Count 1 -Quiet)'
    check = Powershell_execution(command)
    if 'True' in check:
        print(addr, "is up!\n")
