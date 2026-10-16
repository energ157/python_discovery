import subprocess
from Menu import mainMenu
from Discovery import detectAdaptersAndDiscover






    
    

def Main():
    
    print(r"""
▓▓▓▓▓ ▓   ▓ ▓▓▓▓▓ ▓▓▓▓   ▓▓▓    ▓   ▓▓▓▓▓ ▓▓▓▓▓ 
▓     ▓▓  ▓ ▓     ▓   ▓ ▓      ▓▓   ▓         ▓ 
▓▓▓▓  ▓ ▓ ▓ ▓▓▓▓  ▓▓▓▓  ▓  ▓▓   ▓   ▓▓▓▓     ▓  
▓     ▓  ▓▓ ▓     ▓  ▓  ▓   ▓   ▓       ▓   ▓   
▓▓▓▓▓ ▓   ▓ ▓▓▓▓▓ ▓   ▓  ▓▓▓   ▓▓▓  ▓▓▓▓   ▓    
""")
    choice = mainMenu()
    detectAdaptersAndDiscover(choice)
        
    


    

Main()
    
