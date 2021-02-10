
# By @danish_00

from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import CMD_HELP

@register(outgoing=True, pattern=".bin ?(.*)")
async def _(event):
    if event.fwd_from:
        return 
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Searching ur bin 😅😁...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/bin {}".format(danish))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
    
@register(outgoing=True, pattern=".vbv ?(.*)")
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/vbv {}".format(danish))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
              
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
    
@register(outgoing=True, pattern=".key ?(.*)")
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/key {}".format(danish))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
  
@register(outgoing=True, pattern=".iban ?(.*)")
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/iban {}".format(danish))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
             
CMD_HELP.update(
    {
        "binner": ">`.bin`"
        "\nUsage: Buat bin cc njing"
        "\n\n>`.vbv`"
        "\nUsage: Gatau dah vcs kali xixixi."
        "\n\n>`.key`"
        "\nUsage: Kunci kayanya gatau kunci surga mungkin."
        "\n\n>`.iban`"
        "\nUsage: biasa nya yang ada ban ban ny itu banned"
        
        
    }
)
