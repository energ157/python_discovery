
def takeChoiceMenu():
    print("Welcome to the Network Discovery Program")
    print("(1) Discover Live Hosts only")
    print("(2) Discover Open Ports & Live Hosts")
    valid = False
    while not valid:
        try:
            choice = int(input("Choice:>"))
            if choice == 1 or choice == 2:
                valid = True
        except:
            pass
    return choice


def mainMenu():                
    return takeChoiceMenu()

