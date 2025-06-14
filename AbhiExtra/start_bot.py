from pyrogram.types import BotCommand


async def start_bot(Client):
    await Client.start()
    try:
        x = await Client.get_me()
        print(f"Client - [INFO]: @{x.username} get started ")
    except Exception as e:
        print(f"Error - {e}")
    try:
        print("Settings All Commands")
        await Client.set_bot_commands(
            [
                BotCommand("start", "☆ sᴛᴀʀᴛ ʙᴏᴛ ʙʏ ᴀɴʏᴏɴᴇ ☆"),
                BotCommand("ping", "☆ ᴄʜᴇᴄᴋ ᴛʜᴀᴛ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ ☆"),
                BotCommand("banall", "☆ ʙᴀɴᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀ ɪɴ ɢʀᴏᴜᴘ ☆"),
                BotCommand("birthday", "☆ sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʙɪʀᴛʜᴅᴀʏ ᴍᴇssᴀɢᴇ ☆"),
                BotCommand("restart", "☆ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ☆"),
                BotCommand("eval", "☆ ʀᴜɴ ᴘʏᴛʜᴏɴ ᴄᴏᴅᴇ ☆"),
                BotCommand("exec", "☆ ɪɴsᴛᴀʟʟ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴍᴇɴᴛs ☆"),
                BotCommand("gm", "☆ sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴍᴇssᴀɢᴇ ☆"),
                BotCommand("ga", "☆ sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ ᴍᴇssᴀɢᴇs ☆"),
                BotCommand("gn", "☆ sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴍᴇssᴀɢᴇs ☆"),
                BotCommand("raid", "☆ sᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʀᴀɪᴅ ☆"),
                BotCommand("rraid", "☆ sᴛᴀʀᴛ ᴛʜᴇ ʀᴀɪᴅ ɪɴ ᴄʜᴀᴛ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴘᴇʀsᴏɴ ☆"),
                BotCommand("draid", "☆ sᴛᴏᴘ ᴛʜᴇ ʀᴀɪᴅ ɪɴ ᴄʜᴀᴛ ☆"),
                BotCommand("listraid", "☆ ᴄʜᴇᴄᴋ ᴛʜᴇ ʟɪsᴛ ᴏɴ sᴛᴀʀᴛᴇᴅ ʀᴀɪᴅ ᴏɴ ɪᴛ ☆"),
                BotCommand("shayri", "☆ sᴘᴀᴍ ɪɴ ᴄʜᴀᴛ ᴡɪᴛʜ sʜᴀʏʀɪ ☆"),
                BotCommand("stop", "☆ ᴛᴏ sᴛᴏᴘ ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ,ʀᴀɪᴅ,ᴀʙᴜsᴇ ☆"),
                BotCommand("dspam", "☆ sᴛᴀʀᴛ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ᴅᴇʟᴀʏ sᴘᴀᴍ ☆"),
                BotCommand("pspam", "☆ ᴘᴏʀɴsᴘᴀᴍ ᴡɪᴛʜ ʀᴀɪᴅ ☆"),
                BotCommand("hang", "☆ sᴛᴀʀᴛ ʜᴀɴɢ ᴄᴏᴍᴍᴀɴᴅ ᴜsᴇᴅ ᴛᴏ ʜᴀɴɢ ᴛʜᴇ ᴄʜᴀᴛ ☆"),
                BotCommand("uspam", "☆ sᴛᴀʀᴛ ᴛʜᴇ sᴘᴀᴍ ᴛɪʟʟ ᴜsᴇᴅ ᴄᴏᴍᴍᴀɴᴅ sᴛᴏᴏ ☆"),
                BotCommand("uraid", "☆ sᴛᴀʀᴛ ᴛʜᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴀɪᴅ ☆"),
                BotCommand("abuse", "☆ sᴛᴀʀᴛ ᴀʙᴜsɪɴɢ ɴᴏɴ sᴛᴏᴘ ☆"),
                BotCommand("echo", "☆ ᴇᴄʜᴏ ᴛʜᴇ ʀᴇᴘʟʏ ᴍsɢ ☆"),
                BotCommand("help", "☆ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅ ᴄʜᴇᴄᴋ ☆"),
                BotCommand("ceo_of_secularism", "☆ ʙᴏᴛ ᴏᴡɴᴇʀ ☆")
            ]
        )
    except:
        pass

