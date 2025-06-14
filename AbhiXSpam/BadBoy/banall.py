from AbhiExtra.banall import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message

from AbhiXSpam.Config import *

from .. import sudos


@Client.on_message(filters.user(sudos) & filters.command(["banall"], prefixes=HANDLER))
async def banall(AbhiXSpam: Client, message: Message):
    if message.chat.id == message.from_user.id:
        await message.reply_text("Use this cmd in group;")
        return
    await start_banall(AbhiXSpam, message)
