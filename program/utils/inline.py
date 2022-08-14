""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="• الـتـحكـم♪", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="• السورس", url=f'https://t.me/SOURCE_ARBAWY305'),
    ],
    [
    InlineKeyboardButton(
                        "♡اضـف الـبـوت لـمـجـمـوعـتـك♡",
                        url=f'https://t.me/{BOT_USERNAME}?startgroup=true'),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹ ايقاف", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="⏸ وقف مؤقت", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▶️ استئناف", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇 كتم", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="🔊 الغاء الكتم", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="•رجوع", callback_data="cplaym"),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 رجوع", callback_data="cbmenu"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 رجوع", callback_data="cbmenu"
      )
    ]
  ]
)
