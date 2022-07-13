import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')
 
import requests
bit = platform.architecture()[0]
if bit == '32bit':
    print("\x1b[1;92mCongratulations your mobile Support This Tools")
    from OK import login
    login()
elif bit == '64bit':
    os.system('xdg-open https://wa.me/+2347013107449')
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
 
