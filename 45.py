#KAKASHI HATAKE USERBOT
# @C2C_C

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
a = "__________________________"
print("\033[1;31m  SOURCE KAKA\033[2;34mSHI HATAKE")
print(a)
print("")

APP_ID = int(input("\033[1;31m- ENTER APP ID : "))
API_HASH = input("\033[2;34m- ENTER API HASH : ")
print("\n---------------------------")

with TelegramClient(StringSession(), APP_ID, API_HASH) as tb:
    print("")
    print("\n---------------------------")
    print("")
    print("You Will get STRING SESSION  in save msg")
    jmth = tb.send_message("me", f"{tb.session.save()}")
    jmth.reply("هذا هو  كود التيرمكس الخاص بك.\n المطور - @C2C_C ")