from os import system, sys 
from colorama import Fore, Back, Style
from time import sleep
from pyfiglet import figlet_format
green="\033[1;92m"
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
green="\033[1;92m"
red ="\033[1;91m"
blue="\033[1;94m"
pink="\033[1;95m"
yellow="\033[1;93m"
white="\033[1;00m"
OF = "\033[0m"
ww = "\033[0;100m" 

bnr = (Fore.CYAN+f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢀⣼⣿⣷⣦⠀⠀⠀⠀⠀⣠⣿⣷⣄⠀⠀⠀⢰⣿⣷⡀⠀⠀⠀⠀⢀⣴⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⠋⢻⣿⣿⣧⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠀⠀⠀⣠⣾⣿⣿⣿⣿⠃⠀⠀⣿⣿⣿⡇⠀⠀⣤⣴⣿⣿⠟⢿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣿⠁⠀⢘⣿⣿⣿⣤⣦⡀⠀⢀⣼⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⠀⠀⣸⣿⣿⡿⠀⠀⢠⣿⣿⣿⢃⣀⣤⣿⣿⣿⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⣼⣿⣿⡟⠻⣿⣿⣿⣿⡿⠟⠋⢸⣿⣿⡏⠀⠀⣿⣿⣿⠇⠀⠀⣼⣿⣿⣿⣿⣿⡿⠿⠛⠁⠀⠀⠀
⠀⠀⣼⣿⣿⡿⠁⠙⠛⠛⠛⠉⣿⣿⣿⡆⠀⢸⣿⣿⡿⠀⠀⠈⠉⠉⠁⠀⠀⠀⣼⣿⣿⠇⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣥⣀⠀⠀⠀⠀⠀⠀
⠀⠐⣿⣿⣿⠃⠀⠀⠀⠀⠐⢿⣿⣿⡿⠁⠀⢸⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡏⠀⠀⠀⢿⣿⣿⡀⠀⠸⣿⣿⡟⠙⢿⣿⣿⣿⣿⣶⣦⠀⠀
⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠉⠛⠉⠀⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠈⠛⠋⠀⠀⠀⠙⠋⠀⠀⠀⠈⠙⠛⠿⠿⠟⠀⠀
""")
for i in bnr:
  sys.stdout.write(i)
  sys.stdout.flush()
print()
print()
print()
print()
sleep(2)
khosh = (f"""{pink} ~~~~> {green}hello im amir bazmandeh welcome to my scrip
{yellow} ~~~~> {red} thank you for choosing this script
         """)
for i in khosh:
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.001)
print()
print()
print()
print()
sleep(2)
bnrq = input(Fore.CYAN+f"""
shoma braye kodam hozeh az in script stfadeh mikonid

{pink}(1) cyberi
{yellow}(2) filtering
{blue}lotfan adad mored nazar khod ra vared konid ~~~> : """)

print(bnrq)

if bnrq == "1":
    print()
    print()
    print()
    print()
    print(Fore.LIGHTYELLOW_EX+figlet_format("Ok waite"))
    print()
    sleep(3)
    print()
    print()
    print()
    system("python bnr-cyberi.py")
    
if bnrq == "2":
    print()
    print()
    print()
    print()
    print(Fore.LIGHTYELLOW_EX+figlet_format("Ok waite"))
    print()
    sleep(3)
    print()
    print()
    print()
    system("python bnr-filterig.py")