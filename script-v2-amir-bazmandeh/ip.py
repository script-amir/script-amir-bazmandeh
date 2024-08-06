from colorama import Fore 
from os import system
import socket
from time import sleep
system("clear")
site = input(Fore.LIGHTCYAN_EX+"Enter targer site ~~> : ")
ip = socket.gethostbyname(site)
sleep(2)
print("[+] your target ip ~~~> ", ip)