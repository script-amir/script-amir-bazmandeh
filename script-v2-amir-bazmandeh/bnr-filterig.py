from os import system, sys 
from colorama import Fore, Back, Style
from time import sleep
from pyfiglet import figlet_format
system("clear")
green="\033[1;92m"
red ="\033[1;91m"
blue="\033[1;94m"
pink="\033[1;95m"
yellow="\033[1;93m"
white="\033[1;00m"
OF = "\033[0m"
ww = "\033[0;100m" 

bnr = input(Fore.LIGHTCYAN_EX+f"""az kodam abzar zir mikhahid stefadeh konid
{red} (1) mskhlotgar
{green} (2) ajzaye filtering
{blue} (3) gereftan code filtering
{pink} lotfan addad mored nazar ra vared konid ~~> : """)

if bnr =="1":
    print()
    print()
    print()
    print(figlet_format("waite"))
    sleep(3)
    print()
    system("python makhlotgar.py")
    
if bnr =="2":
    print()
    print()
    print()
    print(figlet_format("waite"))
    sleep(3)
    print()
    system("python ajza.py")
    
if bnr =="3":
    print()
    print()
    print()
    print(figlet_format("waite"))
    sleep(3)
    print()
    system("python code-filtering.py")