# this bot openSoure in protect from telegram Account ...

from logging import fatal
from pyrogram import Client , filters

api_id = 6148729
api_hash = "c53cf9fd8f534a0c0a176cc0723bf42f"

app = Client("my_account", api_id, api_hash)
    

check = True
find = list()

@app.on_message(filters.text & filters.private)
def dontSend(client, message):
    contact = app.get_contacts()
    firstname = message.from_user.first_name
    
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
            message.reply_text(f"""سلام {firstname} عزیز
    شما جزي از مخاطبین هستید و اجازه شروع چت را دارید 👨🏽‍🎤""")
            
            

    if check :
        message.delete()
        output = """🧠 برای گفتگو می‌توانید با ایمیل mehranalambeigi@protonmail.com در ارتباط باشید :) اگر سوالی دارید حتما تو فروم ها و سایت هایی مثل StackOverflow بپرسید بهتر جواب میگیرید :)

    💠 لطفا از ارسال پیام به حساب شخصی و کاری اکیدا خودداری کنید.

    💎اگر پروژه ای دارید ایمیل بهترین راهه ::)

    🔰 این پیام به‌صورت خودکار ارسال شده است ، درصورت لزوم می‌توانید با ارسال کد زیر در ایمیل، محتوای آن را اطلاع‌رسانی کنید

    Ray ID : __b462dd137252be0de9ee4b2c256d770c__

    @Mehranirc"""

        message.reply_text(output)
            

    

app.run() 
