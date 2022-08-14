# Copyright (C) 2022 By Shadow

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("الصفحه الرئيسيه")
    await query.edit_message_text(
        f"""✨ **مرحبا عزيزي »「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」!**\n
💭 **᥀︙انا بوت استطيع تشغيل الاغاني والموسيقى في المكالمات  الصوتية! 

᥀︙ لمعرفة اوامر هذا البوت اضغط على » ‹ الاوامر ›!

᥀︙ لمعرفة طريقة تشغيل هذا البوت اضغط على » طريقة التشغيل!
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("طريقة التشغيل", callback_data="cbhowtouse")
                    ],
                [
                    InlineKeyboardButton("‹ الاوامر  › ", callback_data="cbcmds"),
                    InlineKeyboardButton("❤️ المطور", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "‹ كروب الدعم ›", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "‹ قناة السورس ›", url=f"https://t.me/SOURCE_ARBAWY305"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "ضيـف البـوت لمجمـوعتـك ✅",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("طريقة الاستخدام")
    await query.edit_message_text(
        f""" الدليل الأساسي لاستخدام هذا البوت:

 1 ↤ أولاً ، أضفني إلى مجموعتك
 2 ↤ بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي
 3 ↤ بعد ترقيتي ، اكتب `تحديث` مجموعة لتحديث بيانات المشرفين
 4 ↤ أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب انضم لدعوة حساب المساعد
 5 ↤ قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى
 6 ↤ في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر `تحديث` في إصلاح بعض المشكلات
 📌 إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب `مغادره` ثم اكتب `انضم` مرة أخرى

 💡 إذا كانت لديك أسئلة  حول هذا البوت ، فيمكنك إخبارنا منن خلال قروب الدعم الخاصة بي هنا ↤ @{GROUP_SUPPORT}

⚡ قناة البوت @{UPDATES_CHANNEL}
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("قائمة الاوامر")
    await query.edit_message_text(
        f"""» **قم بالضغط علي الزر الذي تريده لمعرفه الاوامر لكل فئه منهم !**

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر الادمنيه", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 اوامر المطور", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 اوامر اساسيه", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("الاوامر الاساسيه")
    await query.edit_message_text(
        f"""🏮 الاوامر الاساسيه:

» `شغل` +「اسم الأغنية / رابط」لتشغيل اغنيه في المحادثه الصوتيه
» `فيديو` +「اسم الفيديو / رابط 」 لتشغيل الفيديو داخل المكالمة
» `مباشر` 「رابط」 تشغيل فيديو مباشر من اليوتيوب
» `القائمه` 「تظهر لك قائمة التشغيل」
» `انهاء` 「لإنهاء الموسيقى / الفيديو في الكول」
» `بحث` + 「 الاسم تنزيل صوت من يوتيوب 」
`»تنزيل` + 「الاسم  تنزيل فيديو من يوتيوب 」
» `تخطي` 「للتخطي إلى التالي」
» `بينج` 「إظهار حالة البوت بينغ」
» `فحص` 「لعرض مده التشغيل للبوت」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("اوامر الادمنيه")
    await query.edit_message_text(
        f"""🏮 هنا أوامر الادمنيه:

» `ايقاف` 「ايقاف التشغيل موقتآ」
» `استئناف` 「استئناف التشغيل」
» `انهاء` 「لإيقاف التشغيل」
» `ميوت` 「لكتم البوت」
» `رفع الكتم` 「لرفع الكتم عن البوت」
» `الصوت` 「ضبط مستوئ الصوت」
» `تحديث` 「لتحديث البوت و قائمة المشرفين」
» `انضم` 「لاستدعاء الحساب المساعد」
» `مغادره` 「لطرد الحساب المساعد」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("اوامر المطور")
    await query.edit_message_text(
        f"""🏮 هنا اوامر المطور:

» `تنظيف` 「حذف جميع الملفات 」
» `السيرفر` 「لمعرفه معلومات السيرفر」
» `ترقيه` 「لتحديث بوتك لاخر نسخه」
» `ريستارت` 「اعاده تشغيل البوت」
» `مغادرة الكل` 「خروج الحساب المساعد من جميع المجموعات」

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ايقاف التشغيل موقتآ\n▶️استئناف التشغيل\n🔇كتم الصوت\n🔊الغاء كتم الصوت\n⏹ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    await query.message.delete()
    

@Client.on_callback_query(filters.regex("cplaym"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("الصفحه الرئيسيه")
    await query.edit_message_text(
        "🏷 **-› الاسم:** [{songname}]({url})\n**⏱ المده:** `{duration}`\n💡 ** الحالة:** `يشغل`\n🎧 **-› مطلوبه من:** {requester}\n📹 ** نوع البث:** `موسيقى`",
                                 
             reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="• التحكم", callback_data="cbmenu"),
                    InlineKeyboardButton(text="•السورس", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(text="• علي", url=f"https://t.me/EL_RAYEQ"),
                    InlineKeyboardButton(text="•حسن", url=f"https://t.me/Dev_Arbawy"),
                ],
                [
                    InlineKeyboardButton(
                        "ضيـف البـوت لمجمـوعتـك ✅",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(text="•اخفاء", callback_data="cls"),
                ],
                
            ]
        ),
    )
