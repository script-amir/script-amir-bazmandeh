import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from colorama import Fore
from os import system

system("clear")
green="\033[1;92m"
yellow="\033[1;93m"

number = input(Fore.LIGHTRED_EX+"[+] Enter your target numbers (+98) ---> : ")
phonenumb = phonenumbers.parse(number)

q = (geocoder.description_for_number(phonenumb, "en"))
w = (carrier.name_for_number(phonenumb, "en"))

print(f"{green}[+] target country ~~~> : ", q)
print(f"{yellow}[+] operator simkart target ~~~> : ", w)
