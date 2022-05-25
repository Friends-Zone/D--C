import asyncio
import time
from collections import deque

from telethon.tl.functions.channels import LeaveChannelRequest

from userbot import CMD_HELP, bot
from userbot.utils import admin_cmd


@borg.on(admin_cmd("leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Lol Group kek!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`But Boss! This is Not A Chat`")


@borg.on(admin_cmd(";__;$"))
async def fun(e):
    t = ";__;"
    for _ in range(10):
        t = f"{t[:-1]}_;"
        await e.edit(t)


@borg.on(admin_cmd("yo$"))
async def Ooo(e):
    t = "yo"
    for _ in range(15):
        t = f"{t[:-1]}oo"
        await e.edit(t)


@borg.on(admin_cmd("Oof$"))
async def Oof(e):
    t = "Oof"
    for _ in range(15):
        t = f"{t[:-1]}of"
        await e.edit(t)


@borg.on(admin_cmd("ccry$"))
# @register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")


@borg.on(admin_cmd("fp$"))
# @register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")


@borg.on(admin_cmd("moon$"))
# @register(outgoing=True, pattern="^.mmoon$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd("heart$"))
# @register(outgoing=True, pattern="^.heart$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd("fap$"))
# @register(outgoing=True, pattern="^.fap$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍆✊🏻💦"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


CMD_HELP.update(
    {
        "extra": ".leave Leave a Chat"
        "\n\n.;__;  You try it!"
        "\n\n.cry  Cry"
        "\n\n.fp Send face palm emoji."
        "\n\n.moon Bot will send a cool moon animation."
        "\n\n.clock  Bot will send a cool clock animation."
        "\n\n.myusernames  List of Usernames owned by you."
        "\n\n.oof Same as ;__; but ooof"
        "\n\n.earth  Sends Kensar Earth animation"
        "\n\n.heart  Try and you'll get your emotions back"
        "\n\n.fap  Faking orgasm"
    }
)
