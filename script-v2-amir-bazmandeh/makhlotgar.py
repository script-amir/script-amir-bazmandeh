from os import sys
from os import system
from time import sleep
from colorama import Fore, Back, Style
from pyfiglet import figlet_format
from datetime import datetime
system("clear")

system("pip install colorama")
system("pip install pyfoglet")
system("pip install datetime")


green="\033[1;92m"
red ="\033[1;91m"
blue="\033[1;94m"
pink="\033[1;95m"
yellow="\033[1;93m"
white="\033[1;00m"
OF = "\033[0m"
ww = "\033[0;100m"

system("clear")

h = (f"""{green}----0%
-------10%
----------20%
-------------30%
----------------40%
-------------------50%
----------------------60%
--------------------------70%
------------------------------80%
---------------------------------90%
------------------------------------100%""")
for i in h:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.01)


sleep(3)
system("clear")
print(Fore.RED+f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠤⠤⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⢀⣀⣀⠀⠠⠤⢀⡑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠅⠒⠈⠉⠀⠀⠀⠀⢀⡀⠀⠘⡀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⢠⣤⣄⡀⠀⢀⣴⡾⠛⠛⠓⠀⢱⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⠉⣩⠻⠖⡘⠛⣴⣶⣦⣤⠴⢄⣧⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠂⠾⠿⠿⠀⣾⡀⠉⠉⠁⠀⠀⠀⣿⠺⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⢿⠇⢠⠠⠤⢠⡤⠂⢸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡠⣖⣁⣻⣶⣾⣥⣤⣴⣿⡏⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡻⡛⣉⣻⣿⡭⠄⢀⠞⠀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣌⠀⠈⣿⡇⠀⠈⡠⠪⠏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠙⢷⡤⠻⠇⠤⠊⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⡔⠁⢠⠀⠀⠙⠢⣀⠀⠀⠀⠀⣠⠇⢳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡀⠤⠀⠒⠊⠉⠀⠀⡇⠀⠘⡄⠀⠀⠀⠈⠑⢢⡤⢼⡁⠀⢸⠀⠉⢶⠠⢀⡀⠀⠀⠀⠀⠀
⡎⠁⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⢻⢦⠀⠀⠀⡴⠋⠀⠀⠙⡄⢸⡆⠀⠈⡄⠀⠈⠉⠐⠢⡄⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠠⠃⠀⠀⠈⡄⠑⣄⡞⢆⠀⠀⢀⠜⠙⠊⢱⠀⠀⠘⡄⠀⠀⠀⠀⠘⡄
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠄⠀⠀⣧⠀⠈⠀⢰⠋⠁⠘⣄⠀⠀⠸⡄⠀⠠⠃⠀⠀⠀⠀⠀⢳
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠐⠀⠂⠒⠐⠒⠀⠀⠂⠒⠒⠒⠒⠐⠂⠒⠀⠒⠂⠀⠀⠀
""")
    
x = datetime.now()

print("time started",x)
                   
print()        
print()     
print()
d = (Fore.GREEN+f"""
{pink}----> Hello 

{yellow}------> welcome to my script

""")
for d in d:
        sys.stdout.write(d)
        sys.stdout.flush()
        sleep(0.03)

print()
print()
a = input(Fore.BLUE+"""
Enter your dxprit ~~> : """)

sleep(1)
print()
print(f"{pink}ok thanks")
print()
print()
sleep(1)

k = input(Fore.BLUE+"""
Enter link sexi ~~> : """)

sleep(1)
print()
print(f"{pink}ok thanks")
print()
print()
sleep(1)

l = input(Fore.BLUE+"""
Enter goid SupportBot ~~> : """)

sleep(1)
print()
print(f"{pink}ok thanks")
print()
print()
sleep(1)

o = input(Fore.BLUE+"""
Enter mokhareb ~~> : """)

sleep(1)
print()
print(f"{pink}ok thanks")
print()
print()
sleep(1)

s = input(Fore.BLUE+"""
Enter link virus ~~> : """)

sleep(1)
print()
print(f"{pink}ok thanks")
print()
print()
sleep(1)

n = input(Fore.BLUE+"""
Enter the algoritm ~~> : """)

sleep(1)
print()
print(f"{pink}ok thanks")
print()
print()
sleep(1)

v = input(Fore.BLUE+"""Enter the bug ~~> : """)

sleep(1)
print()
print(f"{pink}ok thanks")
print()
print()
sleep(1)

print(Fore.WHITE+figlet_format("wait"))

print()
print()
sleep(4)



j = print(f"{green}Your code ~~~》:  👇")

o = print(Back.RED+l,s,a,k,o,n,v,sep="[]")

