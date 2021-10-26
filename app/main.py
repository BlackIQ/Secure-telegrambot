from logging import fatal
from pyrogram import Client , filters

api_id = "1133695614"
api_hash = "YOUR HASH"

app = Client("my_account", api_id, api_hash)
    
check = True
find = list()

@app.on_message(filters.text & filters.private)
def dontSend(client, message):
    contact = app.get_contacts()
    firstname = message.from_user.first_name
    is_bot = message.from_user.is_bot

    if is_bot:
        return
        
    if len(find) >= 1:
        for i in find:
            if i == firstname:
                return

    check = True
    for init in contact:
        if init["first_name"] == firstname:
            check = False
            find.append(firstname)
            message.delete()
            message.reply_text(f"سلام {firstname}\nاکنون آنلاین نیستم. در اولین فرصت بهتون پیام میدم.")

    if check:
        message.delete()
        message.reply_text("🧠 حریم شخصی رو رعایت کنید")

app.run() 
