async def start_banall(Badmunda, message):
    chat = message.chat
    a = await Badmunda.get_chat_member(chat.id, 'me')
    if a.status != "administrator":
        return await Badmunda.send_message(chat.id, "Promote me to admin😭")
    x = await Badmunda.send_message(chat.id, "Hey it's Pb Bot Spam")
    done = 0
    failed = 0
    async for u in Badmunda.get_chat_members(chat.id):
        user = u.user
        try:
            await Badmunda.ban_chat_member(chat.id, user.id)
            done += 1
        except Exception as err:
            print(f"Pb Bot Spam- [INFO]: {str(err)}")
            failed += 1
    await x.delete()
    await Badmunda.send_message(chat.id, f"Members Banned ✓ \n\n Banned {done} users\n failed {failed}")
          
