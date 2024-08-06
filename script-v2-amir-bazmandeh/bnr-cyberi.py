from os import system, sys 
from colorama import Fore, Back, Style
from time import sleep
from pyfiglet import figlet_format
green="\033[1;92m"
red ="\033[1;91m"
blue="\033[1;94m"
pink="\033[1;95m"
yellow="\033[1;93m"
white="\033[1;00m"
OF = "\033[0m"
ww = "\033[0;100m" 
system("clear")

bnr = input(Fore.LIGHTCYAN_EX+f"""az kodam abzar zir mikhahid stefadeh konid
{red} (1) ddos
{green} (2) find ip site
{blue} (3) dar avardan etelaat shomoreh
{pink} lotfan addad mored nazar ra vared konid ~~> : """)

if bnr =="1":
    print()
    print()
    print()
    print(figlet_format("waite"))
    sleep(3)
    print()
    system("python DDos.py")
    
if bnr =="2":
    print()
    print()
    print()
    print(figlet_format("waite"))
    sleep(3)
    print()
    system("python ip.py")

if bnr =="3":
    print()
    print()
    print()
    print(figlet_format("waite"))
    sleep(3)
    print()
    system("python phone.py")   
        
