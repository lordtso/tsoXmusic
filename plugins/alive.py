import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/39e3f1b21cbfa8508a6db.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ ꜰᴀꜱᴛᴇʀ ᴠᴄ  ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌸 ᴏᴡɴᴇʀ 🌸", url="https://t.me/ROCKSTAR_PRINCE_OP")
                  ],[
                    InlineKeyboardButton(
                        "💡 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Sanki_BOTs"
                    ),
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ 🎈", url="https://github.com/TheFelliX/SakshiXMusic"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "⁉️ ʜᴇʟᴘ ‼️", url="https://telegra.ph/R%E1%B4%87%E1%B4%85-L%C9%AA%C9%A2%CA%9C%E1%B4%9B-M%E1%B4%9Cs%C9%AA%E1%B4%84-S%E1%B4%87%CA%80%E1%B4%A0%E1%B4%87%CA%80-04-12"
                    )]
            ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/39e3f1b21cbfa8508a6db.jpg",
        caption=f"""𝑺𝒂𝒌𝒔𝒉𝒊 𝑿 𝑴𝒖𝒔𝒊𝒄 𝑰𝒔 𝑨𝒍𝒊𝒗𝒆 𝑩𝒂𝒃𝒚...""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💡 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Sanki_BOTs")
                ]
            ]
        )
   )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/39e3f1b21cbfa8508a6db.jpg",
        caption=f"""𝑺𝒂𝒌𝒉𝒔𝒊 𝑿 𝑴𝒖𝒔𝒊𝒄 𝑴𝒆𝒏𝒖 𝑹𝒆𝒑𝒐 👅""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❥︎ ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ ❥︎", url=f"https://t.me/MrNitric")
                ]
            ]
        ),
    )
