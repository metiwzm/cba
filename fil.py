# Coded By Metiwz Team
#T.me/Metiwz_Team
#cr : @Metiwz
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.raw import functions
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
from re import match
import random
from datetime import datetime
import os ; os.chdir(os.path.dirname(os.path.abspath(__file__)))
def if_not_exist_creat(filename):
    if not os.path.isfile(filename):
        with open(filename , "w") as f:
            f.write("")
            f.close() 
def write(filename , text):
    with open(filename , "w") as f:
        f.write(text)
        f.close() 
def read(filename):
    with open(filename , "r") as f:
        return f.read()
org = [":", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
fonts = [["เฑพ", "๐ถ", "๐ท", "๐ธ", "๐น", "๐บ", "๐ป", "๐ผ", "๐ฝ", "๐พ", "๐ฟโ"],
["เฑพ", "๐", "๐", "๐", "๐", "๐", "๐", " ๐", "๐", "๐ ", "๐ก"],
["เฑพ", "๐ฌ", "๐ญ", "๐ฎ", "๐ฏ", "๐ฐ", "๐ฑ", "๐ฒ", "๐ณ", "๐ด", "๐ต"],
["เฑพ", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐"],
["เฑพ", "โช","โ ","โก","โข","โฃ","โค","โฅ","โฆ","โง","โจ"],
["เฑพ", "โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ"],
["เฑพ","๐ฌ","๐ญ","๐","โฌ๐โญ", "๐","โค","โฌ๐โญ","๐ฝ","๐ด","โฌ๐โญ"],
["เฑพ","โฐ","ยน","ยฒ","ยณ","โด","โต","โถ","โท","โธ","โน"]]
if_not_exist_creat("timeinname")
if_not_exist_creat("timeinbio")
#----------
api_id = 7273371
api_hash = '553337e711993d5be5dd95b61781eb4b'   
#------โ------
app = Client("meti", api_id, api_hash)
def create_time():
    a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
    ran = random.choice(fonts)
    for char in a :
        a = a.replace(char , ran[int(org.index(str(char)))])
    return a
time = ""
def job():
    global time
    if time != datetime.now(timezone("Asia/Tehran")).strftime("%H:%M"):
        if read("timeinname") == "on":
            try:
                app.send(functions.account.UpdateProfile(last_name=f'| {create_time()}'))
            except Exception as e:
                print(e)
        if read("timeinbio") == "on":
            try:
                app.send(functions.account.UpdateProfile(about=f'๐๐๐ข๐ ๐๐จ โซ [--{create_time()}--] | @Metiwz_Team ๐จ๐ปโ๐ป'))
            except Exception as e:
                print(e)
        time = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
@app.on_message(filters.me and filters.text)
def tool(app, m:Message):
    chat_id, message_id, text = m.chat.id, m.message_id, m.text
    if match(r"^[Hh][Ee][Ll][Pp]$", text):
          app.edit_message_text(m.chat.id , m.message_id , """
โโโโโโฐ**๐๏ธ๐๏ธ๐๏ธ๐๏ธ**โฑโโโฑโ 
โโญโโโโโโโโโโโโโโโโฃ  
โโฃโชผโ `Timebio` -> [ on - off ]
โโฃโชผโ `Timename` -> [ on - off ]
โโฃโชผโ  Cแดแดแดแด Bส Mแดแดษชแดกแดข Tแดแดแด ๐จ๐ปโ๐ป
โโฃโชผโ  @Metiwz | @Metiwz_Team
โโฐโโโโโโโโโโโโโโโโฃ 
โโโโโโโโโโโโโโโฑโ """)
    elif match(r"^[Tt][Ii][Mm][Ee][Nn][Aa][Mm][Ee]$", text.split()[0]):
        if match(r"^[Oo][Nn]$", text.split()[1]):
            write("timeinname", "on")
            app.edit_message_text(chat_id, message_id, "๐๐๐ข๐ ๐๐ฃ ๐๐๐ข๐ [ `แดษด` ]")
        else:
            write("timeinname", "off")
            app.edit_message_text(chat_id, mrssage_id, "๐๐๐ข๐ ๐๐ฃ ๐๐๐ข๐ [ `แดาา` ]")
    elif match(r"^[Tt][Ii][Mm][Ee][Bb][Ii][Oo]$", text.split()[0]):
        if match(r"^[Oo][Nn]$", text.split()[1]):
            write("timeinbio", "on")
            app.edit_message_text(chat_id, message_id, "๐๐๐ข๐ ๐๐ฃ ๐ฝ๐๐ค [ `แดษด` ]")
        else:
            write("timeinbio", "off")
            app.edit_message_text(chat_id, message_id, "๐๐๐ข๐ ๐๐ฃ ๐ฝ๐๐ค [ `แดาา` ]")
scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=5)
scheduler.start()
app.start(), idle(), app.stop()
