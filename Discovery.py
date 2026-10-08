import subprocess
from concurrent.futures import ThreadPoolExecutor
import ipaddress

def Main():
    print("Welcome to the Network Discovery Program")
    Discover()

def Discover():
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
    
def Powershell_execution(command):
    output = subprocess.run(["powershell", "-Command",command],
    capture_output = True,
    text = True,
    creationflags = subprocess.CREATE_NO_WINDOW
    )

    return output.stdout
    

def calculateAdapters():
    Adapters = []
    command = f'(Get-NetIPConfiguration).InterFaceAlias'
    results = Powershell_execution(command)
    for result in results.splitlines():
        Adapters.append(result)

    return Adapters


def calculateIP(Adapter):
    command = f'(Get-NetIPConfiguration | Where-Object {{ $_.InterfaceAlias -eq "{Adapter}" }}).IPv4Address.IPAddress'
    ip = Powershell_execution(command)
    return ip


def calculateSubnet(Adapter):
    command = f'(Get-NetIPConfiguration | Where-Object {{ $_.InterfaceAlias -eq "{Adapter}" }}).IPv4Address.PrefixLength'
    subnetMask = Powershell_execution(command)
    return subnetMask

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

    
    
     

    

Main()
    
