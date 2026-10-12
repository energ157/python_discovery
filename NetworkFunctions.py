from PowerShell import *


def calculateAdapters():
    Adapters = {}
    key = 1
    command = f'(Get-NetIPConfiguration).InterFaceAlias'
    results = Powershell_execution(command)
    for result in results.splitlines():
        Adapters[key] = [result]
        key += 1
    Adapters[key] = ["All Adapters"]
    for key, value in Adapters.items():
        print(f"({key}) {', '.join(value)}")
    return Adapters


def calculateIP(Adapter):
    command = f'(Get-NetIPConfiguration | Where-Object {{ $_.InterfaceAlias -eq "{Adapter}" }}).IPv4Address.IPAddress'
    ip = Powershell_execution(command)
    return ip


def calculateSubnet(Adapter):
    command = f'(Get-NetIPConfiguration | Where-Object {{ $_.InterfaceAlias -eq "{Adapter}" }}).IPv4Address.PrefixLength'
    subnetMask = Powershell_execution(command)
    return subnetMask
