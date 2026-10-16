
def takeChoiceMenu():
    print("Welcome to the Network Discovery Program")
    print("(1) Discover Live Hosts only")
    print("(2) Discover Open TCP Ports & Live Hosts")
    choice= validateNumberChoice([1,2])
    return choice


def mainMenu():                
    return takeChoiceMenu()

def takeChoiceAdapter(Adapters):
    for key, value in Adapters.items():
        print(f"({key}) {', '.join(value)}")

    valid = False
    print("Select an Interface, or select 'All Adapters' to enumerate all interfaces")
    choice = validateNumberChoice(Adapters.keys())

    if Adapters[choice] == 'All Adapters':
        return 999
    return choice

def takeChoiceAPIPA(Adapter):
    print("APIPA Address detected for:", Adapter)
    print("Do you wish to continue? Enumerating the APIPA subnet\nMay take a while and will likely show useless results")
    print("(1) Skip")
    print("(2) Continue (Not Recommended)")
    choice = validateNumberChoice([1,2])
    return choice
    
    

def validateNumberChoice(validNumbers):
    valid = False
    while not valid:
        try:
            choice = int(input("Choice:>"))
            if choice in validNumbers:
                valid = True
        except:
            pass
    return choice
                


def takeChoicePorts():
    print("Select the ports you wish to scan")
    print("(1) Common ports: 1-1023")
    print("(2) All Ports")
    print("(3) Custom ports (You will be prompted to enter the ports shortly)")
    choice = validateNumberChoice([1,2,3])
    if choice == 1:
        return list(range(1,1024))
    if choice == 2:
        return list(range(1,65536))
