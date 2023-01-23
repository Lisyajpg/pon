from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import time
import json

json_cfg = json.loads(open("config.json","r").read())

app = Client("my_account", api_id=json_cfg["api_id"], api_hash=json_cfg["api_hash"])

likework = 0    # Не советую трогать. Это не для настройки!
dislikework = 0 # Не советую трогать. Это не для настройки!

@app.on_message(filters.command(["like"], prefixes=".") & filters.me)
def like(_, msg):
    if msg.reply_to_message:
        global likework
        getreplyid = msg.reply_to_message.id
        getchatid = msg.chat.id
        likework = 1 
        while likework != 0:
            if likework != 0:
                app.send_message(chat_id=getchatid,text="+", reply_to_message_id=getreplyid)
            time.sleep(json_cfg["like_time"])
            
    else:
        msg.edit("Чтобы использовать эту команду, требуется ответить на сообщение")

@app.on_message(filters.command(["likestop"], prefixes=".") & filters.me)
def likestop(_, msg):
    global likework
    if likework != 0:
        likework = 0
        msg.edit("Автоспам лайками отключен")
    else:
        msg.edit("Система не обнаружила автоспам лайками")



@app.on_message(filters.command(["dislike"], prefixes=".") & filters.me)
def dislike(_, msg):
    if msg.reply_to_message:
        global dislikework
        getreplyid = msg.reply_to_message.id
        getchatid = msg.chat.id
        dislikework = 1 
        while dislikework != 0:
            if dislikework != 0:
                app.send_message(chat_id=getchatid,text="-", reply_to_message_id=getreplyid)
            time.sleep(json_cfg["dislike_time"])
            
    else:
        msg.edit("Чтобы использовать эту команду, требуется ответить на сообщение")

@app.on_message(filters.command(["dislikestop"], prefixes=".") & filters.me)
def dislikestop(_, msg):
    global dislikework
    if dislikework != 0:
        dislikework = 0
        msg.edit("Автоспам дизлайками отключен")
    else:
        msg.edit("Система не обнаружила автоспам дизлайками")

print("OK!")
app.run()
