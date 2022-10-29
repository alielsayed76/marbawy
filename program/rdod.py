import asyncio
import os
import time
import pyrogram
from cache.admins import admins
from pyrogram import Client, filters
from config import IMG_3, UPDATES_CHANNEL, OWNER_NAME, SUDO_USERS, BOT_USERNAME, ALIVE_NAME, DEV_NAME
from driver.filters import command, other_filters, other_filters3
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(command(["الإعدادات", "الاعدادات", "اعدادات", f"nftb@{BOT_USERNAME}"]) & other_filters3)
async def nftb(client: Client, message: Message):
    await message.reply(f"""🌀 ها هي اوامر الاغاني :
━━━━━━━━━━━━
⇦اوامر تشغيل البوت في المجموعات⇨
⇦ ✪『 `تشغيل` 』✪➢ ➕ 「اسم الأغنية او / رابط」تشغيل الصوت mp3
⇦ ✪『 `فيديو` 』✪➢ ➕ 「اسم الفديو او / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
⇦ ✪『 `ايقاف او انهاء`』✪➢ ☆ لايقاف التشغيل
⇦ ✪『 `وقف` 』✪➢ ☆ ايقاف التشغيل موقتآ 
⇦ ✪『 `تقدم` 』✪➢ ☆ تخطي الئ التالي
⇦ ✪『 `مواصله` 』✪➢ ☆ استئناف التشغيل 
⇦ ✪『 `ميوت` 』✪➢ ☆ لكتم البوت
⇦ ✪『 `الغاء الكتم`』✪➢ ☆ لرفع كتم البوت
━━━━━━━━━━━━
⇦اوامر التحكم بلبوت خارج وداخل المجموعات⇨
⇦ ✪『 `تحكم` 』✪➢ ☆ ↤ تظهر لك قائمة التشغيل
⇦ ✪『 `بحث` 』✪➢ ➕ «اي شيء تريد البحث عنه بليوتيوب»
⇦ ✪『 `الصوت` 』✪➢ ➕ «كتابه» الرقم لضبط مستوئ الصوت
⇦ ✪『 `تحديث` 』✪➢ ☆ لتحديث البوت و قائمة المشرفين
⇦ ✪『 `انضم` 』✪➢ ☆ لاستدعاء حساب المساعد
⇦ ✪『 `مغادرة` 』✪➢ ☆ لطرد حساب المساعد 
━━━━━━━━━━━━
⇦اوامر تحكم المطور⇨
⇦ ✪『 `مسح` 』✪➢ ☆ لمسح جميع الملفات المستخدمه
⇦ ✪『 `معلومات`  』✪➢ ☆ لرؤيه معلومات النظام 
━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [ 
                 InlineKeyboardButton(
                     ALIVE_NAME, url=f"https://t.me/{OWNER_NAME}"), 
                ],
            ]
        ),
    )
    
    
@Client.on_message(command(["ايدي", f"ids@{BOT_USERNAME}", "/id"]) & other_filters3)
def ids(client: Client, message: Message):
    ali = message.reply_to_message
    if ali:
        message.reply_text(
            f"اسمه 🤓: {message.from_user.mention()}\nايديه ☺️: `{message.from_user.id}`\nيوزره 🌚🙈: @{message.from_user.username}")
    else:
        message.reply(
            f"اسمك 🤓❤️: {message.from_user.mention()}\nايديك ☺️: `{message.from_user.id}`\nيوزرك 🌚🙈: @{message.from_user.username}"
        )


@Client.on_message(command([".", f"vgdg@{BOT_USERNAME}"]) & other_filters3)
async def vgdg(client: Client, message: Message):
    await message.reply(
        f""" صلي علي الحبيب ❤️ """
        )


@Client.on_message(command(["رجلي", f"nftbs@{BOT_USERNAME}"]) & other_filters3)
async def nftbs(client: Client, message: Message):
        await message.reply(f"""تتشل يبعيد 😹😹 """)

    
@Client.on_message(command(["انا مين", f"gghpb@{BOT_USERNAME}"]) & other_filters3)
async def gghpb(client: Client, message: Message):
    await message.reply_text(
        f"""💘 ¦ انت روحي » """, 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "انت روح قلبي🐣💘", url=f"tg://settings")
                ]
            ]
        ),
    )
    
    
@Client.on_message(command(["بحبك", "حبق", "حبكك", "بحبق", "حبقق", "بحبكك", f"nftbsa@{BOT_USERNAME}"]) & other_filters3)
async def nftbsa(client: Client, message: Message):
    await message.reply(
        f"""{message.from_user.mention()}بموت فيك يروح قلبي 🥺❤️
        """)
    
    
@Client.on_message(command(["قول", f"echo@{BOT_USERNAME}"]) & other_filters3)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)
    
    
@Client.on_message(command(["المطور", f"motawerf@{BOT_USERNAME}"]) & other_filters3)
async def motawerf(client: Client, message: Message):
    await message.reply(
        f"""❲ Developers Bot ❳
— — — — — — — — —
 𖥔Dev Name :  {DEV_NAME}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        DEV_NAME, url=f"https://t.me/{OWNER_NAME}")
                ],
                [InlineKeyboardButton("🎧اضافه البوت اللي مجموعتك🎧", url=f"http://t.me/{BOT_USERNAME}?startgroup=new"),              
                ]
            ]
        ),
    )


@Client.on_message(command(["رتبتي", f"motaweryj@{BOT_USERNAME}"]) & filters.user(5369052737))
async def motaweryj(client: Client, message: Message):
    await message.reply(
        f"""مبرمج السورس حبيب قلبي 🌚🙈""")


@Client.on_message(command(["رتبتي", f"motawer@{BOT_USERNAME}"]) & filters.user(5463758350))
async def motawer(client: Client, message: Message):
    await message.reply(
        f"""مبرمج السورس حبيب قلبي 🌚💋""")


    
@Client.on_message(command(["مين ضافني", f"nftbst@{BOT_USERNAME}"]) & other_filters3)
async def nftbst(client: Client, message: Message):
    await message.reply(
        f"""انت دخلت بالرابط متعملش نفسك غبي 😒""")
    
    
@Client.on_message(command(["طيب", f"nftbsta@{BOT_USERNAME}"]) & other_filters3)
async def nftbsta(client: Client, message: Message):
    await message.reply(
        f"""فرح خالتك قريب 😹❤️""")
    
    
@Client.on_message(command(["مين", f"meen@{BOT_USERNAME}"]) & other_filters3)
async def meen(client: Client, message: Message):
    await message.reply(
        f"""انا بوت وبحبك 🥺❤️""")

    
@Client.on_message(command(["كداب", f"kdab@{BOT_USERNAME}"]) & other_filters3)
async def kdab(client: Client, message: Message):
    await message.reply(
        f"""انت اللى كدااب يحليتها ❤️😹""")


@Client.on_message(command(["غور", f"ghour@{BOT_USERNAME}"]) & other_filters3)
async def ghour(client: Client, message: Message):
    await message.reply(
        f"""مش هغور غور انت 😒""")


@Client.on_message(command(["غوري", f"ghoure@{BOT_USERNAME}"]) & other_filters3)
async def ghoure(client: Client, message: Message):
    await message.reply(
        f"""مش هغور غور انت 😒""")


