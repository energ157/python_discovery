import subprocess
from concurrent.futures import ThreadPoolExecutor
import ipaddress
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
    if choice == 1:
        detectAdaptersAndDiscover()
        
    


    

Main()
    
