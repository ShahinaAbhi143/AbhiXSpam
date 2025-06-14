from pyrogram.types import InlineKeyboardButton

async def start_cmd(Badmunda):
    x = await Badmunda.get_me()
    START_OP = [
        [
            InlineKeyboardButton(
                text="🌸 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌸", url=f"https://t.me/ceo_of_secularism"
            ),
            InlineKeyboardButton(
                text="💥 sᴜᴘᴘᴏʀᴛ 💥", url=f"https://t.me/imagine_iq"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👻 ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ  👻",
                url=f"https://t.me/{x.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📂 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📂", url=f"https://t.me/imagine_iq"
            ),
            InlineKeyboardButton(
                text="✨ ᴜᴘᴅᴀᴛᴇ ✨", url=f"https://t.me/imagine_iq"
            ),
        ],
    ]
    return START_OP
  
