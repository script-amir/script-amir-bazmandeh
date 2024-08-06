from os import system, sys
system("clear")
system("pip install colorama")
system("pip install pyfiglet")

from pyfiglet import figlet_format
from colorama import Fore, Back, Style
from time import sleep
import random

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
sleep(3)
print(f"""{red}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      
      """)
print("")
print("")
print("")
print("")
sleep(3)

system("clear")

print(Fore.GREEN+figlet_format("Amir"))
print("")
print("")
print("")
print("")

t = input(Fore.CYAN+"""
(1) Jalb konnandeh
(2) hasas konnandeh
(3) code filtering
Enter number ~~~> : """)
print("")
print("")



code =  ['Report.account=["گوید تارکت"]=(<http://dxprit-supportbot-hacker-bakhtiari-fil.phpnet.us/fil.rubika.html>)http://ffmodmenu.page.link/Anti-V+ip.server=("5.106.8.151")sexi-image=["https://s8.uupload.ir/files/08_63n7.jpg"]xxx.com(<B2n.ir/f94037>)please.open.the.link=("http://185.172.128.8/ma.exe")+sexi.mp4=["B2n.ir/sexi.mp4"]+http://linux.io/killd-0000.4-spam%100/bug-3.5.4-linux(<apt onlline Server rubika.ir=["kali-linux_hack=https://rubika.ir/SupportBot"] cd tool-linux=["ddos-linux=rubika.ir"] print ["rm -rf ="تارگت ایدی"]https://pypi.org/project/malware>)https://hacker.house/d///f//i///y.6.0.3.2.3.8.6.4.5.8.6.3.7.7.9.0.5.7.8.9.2.1.3.4.5.6.7.8.9.0.4.3.1.2.3.', 'Check.report.report.account=[" ایدی"]=("https://bilalphilips.com/anti-islaamic-websites")+bug=("https://BuG.in.supportbot/43390ec-.11.11.C4.12.12.-122234-111334-999-99977-000-999909-9999999.C4-777777.g-6065-8085-242425-0000.4-000>)+terrorist={<https://www.dni.gov/nctc/ftos/isis_fto.html>}sexbebin.com=("https://biaupload.com/do.php?imgf=org-824657c28e301.jpg")darkweb-sites.org>(https://horrorescape.com)<http://ffmodmenu.page.link/Anti-V>)http://www.masturbatenchill.com}>sexi.mp4={<https://biaupload.com/do.php?filename=org-dd651490f82b1.mp4>}https://BuG.in.supportbot.rubika.ir/sexbebin.com/RubikaSupportReport-bug-3.5.4-server-Yfttks10-0-yftt15k/4.3.1.0.4.9.9.3.5.6.1.4VmDzA7iaHb.am.am.am', 'Check.report.report.account=[" ایدی"]=("https://bilalphilips.com/anti-islaamic-websites")+bug=("https://BuG.in.supportbot/43390ec-.11.11.C4.12.12.-122234-111334-999-99977-000-999909-9999999.C4-777777.g-6065-8085-242425-0000.4-000>)+terrorist={<https://www.dni.gov/nctc/ftos/isis_fto.html>}sexbebin.com=("https://biaupload.com/do.php?imgf=org-824657c28e301.jpg")darkweb-sites.org>(https://horrorescape.com)<http://ffmodmenu.page.link/Anti-V>)http://www.masturbatenchill.com}>sexi.mp4={<https://biaupload.com/do.php?filename=org-dd651490f82b1.mp4>}https://BuG.in.supportbot.rubika.ir/sexbebin.com/RubikaSupportReport-bug-3.5.4-server-Yfttks10-0-yftt15k/4.3.1.0.4.9.9.3.5.6.1.4VmDzA7iaHb.am.am.am', 'Check.report.report.account=[" ایدی"]=("https://bilalphilips.com/anti-islaamic-websites")+bug=("https://BuG.in.supportbot/43390ec-.11.11.C4.12.12.-122234-111334-999-99977-000-999909-9999999.C4-777777.g-6065-8085-242425-0000.4-000>)+terrorist={<https://www.dni.gov/nctc/ftos/isis_fto.html>}sexbebin.com=("https://biaupload.com/do.php?imgf=org-824657c28e301.jpg")darkweb-sites.org>(https://horrorescape.com)<http://ffmodmenu.page.link/Anti-V>)http://www.masturbatenchill.com}>sexi.mp4={<https://biaupload.com/do.php?filename=org-dd651490f82b1.mp4>}https://BuG.in.supportbot.rubika.ir/sexbebin.com/RubikaSupportReport-bug-3.5.4-server-Yfttks10-0-yftt15k/4.3.1.0.4.9.9.3.5.6.1.4VmDzA7iaHb.am.am.am', 'Check.report.account=["گوید"]=("http://ffmodmenu.page.link/Anti-V")+sexi.mp4={https://imgurl.ir/uploads/u497134_VID_20230401_204306_495.mp4}ip.server=(<5.106.8.151>)http://dxprit-mehrab-sigari-28-hacker.phpnet.us<[B2n.ir/Sex.photo]>xxx.com(<https://freedomhacker.net/top-free-websites-to-learn-hacking-2016-4842>)pornhab.com<[https://hackernoon.com/how-to-create-your-own-dark-website-onion-on-linux]>sexbebin.com("https://www.hacker101.com/playlists/web_hacking.html")=apt install server rubika.ir=["cd kali tools"]=ddos=("web.rubika.ir")+{rm - rfایدی }+please.open.the.link=("https://github.com/gunslinger/Python-VirusTotal-link-scanner/blob/master/main.py")https://BuG.in.supportbot/0×C4,0×100,0.deviantart-bug-0000.4-php-YftTkS-112334/3602036892-yftt15k-17k-18k-yttf20k-Filter-yftt17k.6.2.4.8.1.1.9.5.0.4.4.5.5.4.2.8.6./10.10.34.35-9999999.C400/af.af.f.af.af.af.af.af', 'Cheak.Report.Account={"گوید"}=<{http://ffmodmenu.page.link/Anti-V}sexi-image={"<https://s8.uupload.ir/files/screenshot_۲۰۲۴۰۶۲۵_۲۲۲۸۱۹_gallery_tmku.png>"}sexi-mp4(<https://uploadkon.ir/uploads/db9920_23VID-20231120-222300-343-001.mp4>)anti-khamenei-websites=["https://fa.m.wikipedia.org/wiki/%D9%85%D8%B1%DA%AF_%D8%A8%D8%B1_%D8%AE%D8%A7%D9%85%D9%86%D9%87%E2%80%8C%D8%A7%DB%8C"]xnxx.com("https://linuxsecurity.expert/security-tools/linux-malware-detection-tools")=apt install server rubika.ir=[cd ddos toll]=ddos=("web.rubika.ir")+{<rm -rf=ایدی{"https://jizzbunker-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=fa&_x_tr_hl=fa&_x_tr_pto=sc"}http://hacker.rubika.sex.hacker.1246189591.65.77678886.infect.inxs.com.yttff17.5.2.7.9.7.8.9.2.ytff17.ytff.20.6.0.3.7.9.0.2.3.2-C444/0.0.1.1.1.af.af..af.af.af.am.am.am.am.am.am.am', 'Report account=["گوید"]=(<http://dxprit-mehrab-sigari-28-hacker.phpnet.us>)http://ffmodmenu.page.link/Anti-V+ip.server=("5.106.8.151")sexi-image=["https://biaupload.com/do.php?imgf=org-29fa4625034e1.jpg"]xxx.com(<http://B2n.ir/f94037>)please.open.the.link=("http://185.172.128.8/ma.exe")+sexi.mp4=["https://imgurl.ir/uploads/u497134_VID_20230401_204306_495.mp4"]+https://linux.io/?s=linux.io%2Fkilld-0000.4-spam%25100%2Fbug-3.5.4-linux(<apt onlline Server rubika.ir=["kali-linux_hack=https://rubika.ir/SupportBot"] cd tool-linux=["ddos-linux=rubika.ir"] print ["rm -rf ="تارگت ایدی"]https://2.4.0.1/f////g.h.6.0.2.9.3.8.6.4.7.8.9.2.5.6.8.3.6.8.3.1.8.9.0.3.0.3.4.0.6.7.0.1.4.5.0.1.yttff17.5.2.7.9.7.8.9.2.ytff17.ytff.20.6.0.3.7.9.0.2.3.2-C444/0.0.1.1.1.af.af.af.af.af.af.af.af.af.af.af.af.af', 'Check.report.report.account=["گوید تارگت"]=("https://liveweave.com/JUcnd7")+sexi.mp4={https://imgurl.ir/viewer.php?file=i14338_InShot_20240531_165347424.mp4}ip.server=(<5.106.8.151>)http://B2n.ir/dxprit.sxs-support.bot<[B2n.ir/Sex.photo]>xxx.com(<https://github.com/Rastin666/Dscript-filter-filter-filter-rubika>)B2n.ir/anti-islaamic<[https://python-forum.io/thread-2172.html]>sexbebin.com("https://bugzilla.kernel.org/show_bug.cgi?id=199037")=apt install server rubika.ir=["cd kali tools"]=ddos=("web.rubika.ir")+{rm - rf ایدی تارگت}+please.open.the.link=("http://B2n.ir/Kali.hacker")https://BuG.in.supportbot/0×C4,0×100,0.deviantart-bug-0000.4-php-YftTkS-112334/0.9.0.9.0.9.0-yftt15k-17k-18k-yttf20k-Filter-yftt17k.6.2.4.8.1.1.9.5.0.4.4.5.5.4.2.8.6./10.10.34.35-9999999.C400/af.af.f.af.af.af.af.af', 'please.check.report=sex.dxpr=("https://jsbin.com/rinazaroba/edit?output")+sexi.mp4=["https://uupload.ir/view/inshot_20240531_124125111_a06f.mp4/"]de.pornhub.com<>Report.account={"https://github.com/Tacklorix/Tack-Lorix-/tree/main"}+sexi-image=("https://biaupload.com/do.php?imgf=org-ad13941876f71.jpg")=sexbebin.com<)https://python-forum.io/thread-1051.html<[@SupportBot]>Virus.account=("http://ffmodmenu.page.link/Anti-V")+https://python-forum.io/thread-1051.html>)terrorist={https://www.dni.gov/nctc/ftos/isis_fto.html}ip.server=("5.106.8.151")https://pypi.org/project/hack-anything<[https://linuxsecurity.expert/security-tools/linux-malware-detection-tools]>https://BuG.in.rubika/RubikaSupportReport-bug-3.5.4-server-5.2.1.6.8.1.5.1.5.5.1.2.4.0.3.4.X.0.XX.0.x.Fil/yftt15k/-17k/-18k/-yttf20k/2.6.0.4.2.7.4.1.6.7.1.1.1.3.1.7.2.3.7.4.5.2.5.3.5.3.1.2.3.2.6.9.4.3.7.5.4.9', 'please.check.report=sex.dxpr=("https://jsbin.com/rinazaroba/edit?output")+sexi.mp4=["https://uupload.ir/view/inshot_20240531_124125111_a06f.mp4/"]de.pornhub.com<>Report.account={"https://github.com/Tacklorix/Tack-Lorix-/tree/main"}+sexi-image=("https://biaupload.com/do.php?imgf=org-ad13941876f71.jpg")=sexbebin.com<)https://python-forum.io/thread-1051.html<[@SupportBot]>Virus.account=("http://ffmodmenu.page.link/Anti-V")+https://python-forum.io/thread-1051.html>)terrorist={https://www.dni.gov/nctc/ftos/isis_fto.html}ip.server=("5.106.8.151")https://pypi.org/project/hack-anything<[https://linuxsecurity.expert/security-tools/linux-malware-detection-tools]>https://BuG.in.rubika/RubikaSupportReport-bug-3.5.4-server-5.2.1.6.8.1.5.1.5.5.1.2.4.0.3.4.X.0.XX.0.x.Fil/yftt15k/-17k/-18k/-yttf20k/2.6.0.4.2.7.4.1.6.7.1.1.1.3.1.7.2.3.7.4.5.2.5.3.5.3.1.2.3.2.6.9.4.3.7.5.4.9please.check.report=sex.dxpr=("https://jsbin.com/rinazaroba/edit?output")+sexi.mp4=["https://uupload.ir/view/inshot_20240531_124125111_a06f.mp4/"]de.pornhub.com<>Report.account={"https://github.com/Tacklorix/Tack-Lorix-/tree/main"}+sexi-image=("https://biaupload.com/do.php?imgf=org-ad13941876f71.jpg")=sexbebin.com<)https://python-forum.io/thread-1051.html<[@SupportBot]>Virus.account=("http://ffmodmenu.page.link/Anti-V")+https://python-forum.io/thread-1051.html>)terrorist={https://www.dni.gov/nctc/ftos/isis_fto.html}ip.server=("5.106.8.151")https://pypi.org/project/hack-anything<[https://linuxsecurity.expert/security-tools/linux-malware-detection-tools]>https://BuG.in.rubika/RubikaSupportReport-bug-3.5.4-server-5.2.1.6.8.1.5.1.5.5.1.2.4.0.3.4.X.0.XX.0.x.Fil/yftt15k/-17k/-18k/-yttf20k/2.6.0.4.2.7.4.1.6.7.1.1.1.3.1.7.2.3.7.4.5.2.5.3.5.3.1.2.3.2.6.9.4.3.7.5.4.9', 'Check.report.report.account=["ایدی تارگت"]=("https://bilalphilips.com/anti-islaamic-websites")+bug=("https://BuG.in.supportbot/43390ec-.11.11.C4.12.12.-122234-111334-999-99977-000-999909-9999999.C4-777777.g-6065-8085-242425-0000.4-000>)+terrorist={<https://www.dni.gov/nctc/ftos/isis_fto.html>}sexbebin.com=("https://biaupload.com/do.php?imgf=org-824657c28e301.jpg")darkweb-sites.org>(https://horrorescape.com)<http://ffmodmenu.page.link/Anti-V>)http://www.masturbatenchill.com}>sexi.mp4={<https://biaupload.com/do.php?filename=org-dd651490f82b1.mp4>}https://BuG.in.supportbot.rubika.ir/sexbebin.com/RubikaSupportReport-bug-3.5.4-server-Yfttks10-0-yftt15k/4.3.1.0.4.9.9.3.5.6.1.4VmDzA7iaHb.am.am.am', 'Report.py("http://ffmodmenu.page.link/Anti-V")+ip.server={5.106.8.151}https://bilalphilips.com/anti-islaamic-websites<de.pornhub.com>https://porn.rubika.ir/6.3.1.4.3.1.0.4.9.9.3.5.6.1.1.11.C4.12.12//f//i//l//t//e//r/5.1.4.3.1.0.4.9.9.3.5.6.1.7.4.3.1.0.4.9.9.3.5.6.1<{https://www.dni.gov/nctc/ftos/isis_fto.html}>xxx.com("https://5106.10.266.Filter.account.Rubika.ir/*v3.0.6v")https://3.0.9.yfT115k.in<[https://www.cbc.ca/amp/1.5124240]>https://This.user.is.filtering.filtering.and.threa.ening.to.filter>)please.open.the.link=("http://185.172.128.8/ma.exe")sexi.mp4=(<https://imgurl.ir/uploads/u497134_VID_20230401_204306_495.mp4>)http://web.rubika.ir/#c=b0Y0a2cafbaf668e282d2dc02a1fe2a7', 'Report.channel=("https://999.888.777.666.yttf15/1.4.2.4.8.1.1.9.5.0.4.4.5.5.4.2.8.6.8.1.5.1.5.5.1.2.4.0.3.4.X.0.XX.0.x.Fil.rubika.html")+server=("5.106.8.151")+<[xxx.com]>hacker.house/5.3.1.5.7.3.2.5.2.6.2.7.F.I.L.T.E.R.I.N.G.X.X.X/yftt15k/-17k/-18k/-yttf20k.1.5.4.14-0-7.5-3.36-7.5.7.5s3.36.7.5.2.5.0.2.0.Fil.rubika.ir>}$¥flpom/6489.9.9.9.9.9.9.9.9.9.9.4%¥£.€.₩/9.9.9.9.9.9.9.C4/yftt15k/-17k/-18k/-yttf20k.7.5-7.5-3.36-7.5-7.5-3.36-7.5-7.5-7.5.0..3.5c-3.3.0.7.5.0-6-2.6.9.2.5.6.6.2.92.5.6.6.6.6.2.6.9.2.5.6.2.6.2.5.am.am.am.am.am.am>)https://bUg.FYLLTER/CT.5.106.8.151.IP.SERVER-0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1/yttf20k-yftt15k-yftt10k.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am<Spam%100>+https://spam-000-in.channel.rubika.ircyberpolice.ir.£filter.81.2.8.4.9.2.9.5.2.1.0.1.0.3.4.3.5.Bug.bug.Bug.bug.BUG.cyberpolice.gov.ir', 'Report.py("http://ffmodmenu.page.link/Anti-V")+ip.server={5.106.8.151}https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh/>https://porn.rubika.ir/6.3.1.4.3.1.0.4.9.9.3.5.6.1.1.11.C4.12.12//f//i//l//t//e//r/5.1.4.3.1.0.4.9.9.3.5.6.1.7.4.3.1.0.4.9.9.3.5.6.1.3.9.0.2.3.-999999-777777.1.3<{https://www.dni.gov/nctc/ftos/isis_fto.html}>xxx.com("https://5106.10.266.Filter.account.Rubika.ir/*v3.0.6v")http://dxprit-dani-hack.xlphp.net]>https://This.user.is.filtering.filtering.and.threa.ening.to.filter>)please.open.the.link=("http://185.172.128.8/ma.exe")sexi.mp4=(<https://imgurl.ir/uploads/u497134_VID_20230401_204306_495.mp4>)("http://dxprit-sxs-support-bot-hsck-fil.phpnet.us/fuk.sxs.photos.html")http://sexbebin.com/3.5.4.c-0x0.0x0.0x0.0x0.0x0.0x0.0x0.0x0.0x0.OF.OF.OF.OF.OF.OF.OF.OF.OF.OF.OF.OF/0.9.0.9.0.9.0.9.0.9.0.9/filtet.af.af.af/Filterig_account/¥fttks-C444.0.0.1.am.am.am.am.am.am', 'Check.report.report.account=["ایدی تارگت"]=("https://bilalphilips.com/anti-islaamic-websites")+bug=("https://BuG.in.supportbot/43390ec-.11.11.C4.12.12.-122234-111334-999-99977-000-999909-9999999.C4-777777.g-6065-8085-242425-0000.4-000>)+terrorist={<https://www.dni.gov/nctc/ftos/isis_fto.html>}sexbebin.com=("https://biaupload.com/do.php?imgf=org-824657c28e301.jpg")darkweb-sites.org>(https://horrorescape.com)<http://ffmodmenu.page.link/Anti-V>)http://www.masturbatenchill.com}>sexi.mp4={<https://biaupload.com/do.php?filename=org-dd651490f82b1.mp4>}https://BuG.in.supportbot.rubika.ir/sexbebin.com/RubikaSupportReport-bug-3.5.4-server-Yfttks10-0-yftt15k/4.3.1.0.4.9.9.3.5.6.1.4VmDzA7iaHb.am.am.am', 'Report.py("http://ffmodmenu.page.link/Anti-V")+ip.server={5.106.8.151}https://www.merriam-webster.com/dictionary/anti-Islamic-websites<de.pornhub.com>https://Support.bot/1.3.5.4/gk//DarkWeb-000-tor//15k/3.3.3.1.0.1.0.3.Kmni.4.3.5.1.3.1.0.7.2.4.6.3.5.1.0.1.0.3.4.3.4//9.1.5.3/-Cyberpolice.gov.ir<{https://python-forum.io/thread-1051.html}>xxx.com("https://5106.10.266.Filter.account.Rubika.ir/*v3.0.6v")https://3.0.9.yfT115k.in[https://media.ccc.de/c/22c3/Hacking]>https://This.user.is.filtering.filtering.and.threa.ening.to.filter>)please.open.the.link=("http://185.172.128.8/ma.exe")sexi.mp4=(<https://uploadkon.ir/uploads/e8ef08_24VID-20240506-204800-619.mp4>)http://web.rubika.ir/#c=b0Y0a2cafbaf668e282d2dc02a1fe2a7', 'Cheak.Report.Account={"گوید"}=<{http://ffmodmenu.page.link/Anti-V}sexi-image={"<https://s8.uupload.ir/files/screenshot_۲۰۲۴۰۶۲۵_۲۲۲۸۱۹_gallery_tmku.png>"}sexi-mp4(<https://uploadkon.ir/uploads/db9920_23VID-20231120-222300-343-001.mp4>)anti-khamenei-websites=["https://fa.m.wikipedia.org/wiki/%D9%85%D8%B1%DA%AF_%D8%A8%D8%B1_%D8%AE%D8%A7%D9%85%D9%86%D9%87%E2%80%8C%D8%A7%DB%8C"]xnxx.com("https://linuxsecurity.expert/security-tools/linux-malware-detection-tools")=apt install server rubika.ir=[cd ddos toll]=ddos=("web.rubika.ir")+{<rm -rf=ایدی{"https://jizzbunker-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=fa&_x_tr_hl=fa&_x_tr_pto=sc"}http://hacker.rubika.sex.hacker.1246189591.65.77678886.infect.inxs.com.yttff17.5.2.7.9.7.8.9.2.ytff17.ytff.20.6.0.3.7.9.0.2.3.2-C444/0.0.1.1.1.af.af..af.af.af.am.am.am.am.am.am.am', 'http://Check.report.account>(@SupportBot)=["http://ffmodmenu.page.link/Anti-V"]+{https://iranwire.com/en/politics/126281-in-a-first-un-report-implicates-ali-khamenei-in-crimes-against-humanity}ip.server=>5.106.8.151<http://dxprit-dani.xlphp.net<[B2n.ir/Sex.photo]>xxx.com<http://noobhacktube.com>)pornhab.com<[https://imgurl.ir/uploads/u73287_VID_20240302_170745_435.mp4]>sexbebin.com["https://dynamicbusiness.com/locked/norton-reveals-100-most-dangerous-websites4168.html"]=["web.rubika.ir")+{rm-rf={@ایدی}+please.open.the.link=("https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh")http://server.3.5.4.c-0x0.0x0.0x0.0x0.0x0.0x0.0x0.0x0.0x0.0x0.0×0.C444/99999-77777.0.2.1.9.9.0.9.0.7.7.7.7.7.9.0.af.af.af.af.af.af.af.af.af.af.af.af.af.af.af.af', 'hack.report account =["ایدی "]{http://ffmodmenu.page.link/Anti-V}sexi-image={"<https://up.20script.ir/file/2f7c-InShot-۲۰۲۳۰۹۱۳-۱۹۴۹۵۸۹۸۷.jpg>"}sexi-mp4(<https://imgurl.ir/uploads/u73287_VID_20240302_170745_435.mp4>)anti-khamenei-websites=["https://iranwire.com/en/politics/126281-in-a-first-un-report-implicates-ali-khamenei-in-crimes-against-humanity/"]xnxx.com("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip")apt onlline Server rubika.ir=["kali-linux_hack=https://rubika.ir/SupportBot"]cd tool-linux=["ddos-linux=rubika.ir"]print["rm -rf ="ایدی"]{"https://0x00sec.org/t/malware-reversing-burpsuite-keygen/5167"}http://hacker.rubika.sex.hacker.1246189591.65.77678886.infect.inxs.com.yttff17.5.2.7.9.7.8.9.2.ytff17.ytff.20.6.0.3.7.9.0.2.3.2-C44/99999-77777-1.2.3.9.af.af.af.af.af.af.af.af.af.af.af', 'Report.account=["گوید"]=("http://ffmodmenu.page.link/Anti-V")+sexi.mp4={https://imgurl.ir/uploads/u497134_VID_20230401_204306_495.mp4}ip.server=(<5.106.8.151>)http://dxprit-mehrab-sigari-28-hacker.phpnet.us<[B2n.ir/Sex.photo]>xxx.com(<https://rb.ru/search/?query=https%3A%2F%2F2aE.xyz%2FIG%2FigV2%3Fref%3D5342>)pornhab.com<[https://dzen.ru/a/XoSlrMUtAj2MlY5R]>sexbebin.com("https://rb.ru/search/?query=http%3A%2F%2Fwww.sepahnews.com%2F")=apt install server rubika.ir=["cd kali tools"]=ddos=("web.rubika.ir")+{rm - rf ایدی}+please.open.the.link=("https://dzen.ru/a/XsV_QPbbnglm8NTz")https://BuG.in.supportbot.rubika.ir/sexbebin.com/RubikaSupportReport-bug-3.5.4-server-Yfttks10-0-yftt15k/4.3.1.0.4.9.9.3.5.6.1.4VmDzA7iaHb.am.am.am']
jalb = ['https://check.report.SupportBot/check/Report.account/http://web.rubika.ir/#c=b0Y0a2cafbaf668e282d2dc02a1fe2a7/185.201.49.247/5.106.8.151/please.check.report<(@SupportBot=https://rubika.ir/SupportBot=/Spam_Account.bot)', 'https://check.report.SupportBot/check/Report.account/http://web.rubika.ir/#c=b0Y0a2cafbaf668e282d2dc02a1fe2a7/185.201.49.247/5.106.8.151/please.check.report']
hasas = ['Report.account=("ffmodmenu.page.link/Anti-V")+terrorist={<https://www.rand.org/topics/the-islamic-state-terrorist-organization.html>}sexy.jpg=("https://s8.uupload.ir/files/8-2-640x360_4yrg.jpg")+dark.web=["https://xgore.net/a-policeman-was-killed-and-butchered-like-an-animal/"]xxx.com>(https://3dnews.ru/1009634/10-samih-vpechatlyayushchih-kiberatak-v-istorii)>http://sexbebin.com/3.5.4.c-0x0.0x0.0x0.0x0.0x0.0x0.0x0.0x0.0x0.filtet.af.af.af/Filterig_account/¥fttks-C444.0.0.1.am.am.am.am.am.am<de.pornhub.org>https://web.rubika.ir/#c=b0Y0a2cafbaf668e282d2dc02a1fe2a7', 'Report.account=["گوید طرف"]=["This user uses provocative and obscene profiles"]=virus.account=("https://liveweave.com/JUcnd7")=#Spam%100>(sexy.mp4=("https://imgurl.ir/uploads/w81562_InShot_20240312_170543691.mp4")https://hacker.house/d///f//i///y.6.0.3.2.3.8.6.4.5.8.6.3.7.7.9.0.5.7.8.9.2.1.3.4.5.6.7.8.9.0.4.3', 'Report.account=["گوید طرف"]=This user has a provocative profile and is provocative>)https://web.rubika.ir/main-es5.62d23c44983e1a4f3a57.js<[xxx.com]><Filter>Sincerely, this user uses a provocative profile that provokes male users. please check it.>}https://web.rubika.ir/#c=b0Y0a2cafbaf668e282d2dc02a1fe2a7', 'please.rheck.report.account=Report.account=["https://hackread.com/doctor-bitcoin-dark-web-hitman/"]https://github.com/java-virus<sexbebin.com>#spam%100=["https://github.com/java-virus"]+anti.Islam.website={<https://en.m.wikipedia.org/wiki/Islamic_State>}https://www.gunsinternational.com<[xxx.com]>https://anonymoushackers.net/0.9.09.0.9.0.9.0.9.0.9.0.9.0.9.0.9.0.9.0.9.0.9.0.9.0.9.0.9.0/hacker.com/1.5.9.4.2.4.9.2.4.9.4.1.5.2.4/report.account']

if t =="1":
    print("")
    print("")
    print(Fore.YELLOW+"for you 👇")
    print("")
    print("")
    sleep(4)   
    print(Fore.RED+random.choice(jalb))
    print("")
    print("")
    print("") 
    sleep(3)
    print(Fore.BLUE+"SaEeD ~~> Bye")
    
if t =="2":
    print("")
    print("")
    print(Fore.YELLOW+"for you 👇")
    print("")
    print("")
    sleep(4)   
    print(Fore.RED+random.choice(hasas))
    print("")
    print("")
    print("") 
    sleep(3)
    print(Fore.BLUE+"SaEeD ~~> Bye")
    
if t =="3":
    print("")
    print("")
    print(Fore.YELLOW+"for you 👇")
    print("")
    print("")
    sleep(4)   
    print(Fore.RED+random.choice(code))
    print("")
    print("")
    print("") 
    sleep(3)
    print(Fore.BLUE+"SaEeD ~~> Bye")