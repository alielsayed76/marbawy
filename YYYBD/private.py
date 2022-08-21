from pyrogram import filters, Client
from pyrogram.errors import BotInlineDisabled
from driver.veez import user as USER
from config import SUDO_USERS, BOT_USERNAME
ADMINS=SUDO_USERS

@USER.on_message(filters.private & ~filters.bot & filters.incoming & ~filters.service & ~filters.me)
async def reply(client, message): 
    try:
        inline = await USER.get_inline_bot_results(BOT_USERNAME, "inline_ass_by_ali")
        await USER.send_inline_bot_result(
            message.chat.id,
            query_id=inline.query_id,
            result_id=inline.results[0].id,
            hide_via=True
            )
    except BotInlineDisabled:
        for admin in ADMINS:
            try:
                await USER.send_message(chat_id=admin, text=f"اهلا عزيزي المطور\nلم تقم بتفعيل وضع الانلاين في البوت @{BOT_USERNAME}\n\nيقوم الحساب المساعد باستخدام البوت في الرد علي الاشخاص في الخاص\nويتم استخدام وضع الانلاين في البحث علي يوتيوب")
            except Exception as e:
                print(e)
                pass

    except Exception as e:
        print(e)
        pass

