import os

from telethon import Button, events
from telethon.tl.custom import Button

from userbot import ALIVE_NAME
from userbot import bot as borg

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

TG_BOT_USER_NAME_BF_HER = os.environ.get("ALIVE_PHOTTO", None)
if TG_BOT_USER_NAME_BF_HER is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        ghanti = me.id
        dc_text = f"** 𝙳𝙰𝚁𝙺 𝙲𝙾𝙱𝚁𝙰 MOD 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n✘ About My System ✘\n\n➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.17.5\n➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/Dark_cobra_support)\n➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [The Terminal](https://github.com/The-Terminal)\n➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [The-Terminal](https://github.com/The-Terminal/DARKCOBRA)\n\n➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"
        if query.startswith("dcmod") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/ProgrammingError/D--C"),
                    Button.url(
                        "Deploy",
                        "https://heroku.com/deploy?template=https://github.com/ProgrammingError/D--C/blob/master",
                    ),
                ],
                [
                    Button.url("String", "https://repl.it/@Danish00/DarkCobra#main.py"),
                    Button.url("Channel", "https://t.me/moi_plugs"),
                ],
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    # title="Shivam",
                    text=dc_text,
                    buttons=buttons,
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="DC Mod",
                    text=dc_text,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="DC Mod",
                    text=dc_text,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)


import os
import urllib

from telethon import Button, events
from youtubesearchpython import SearchVideos

from userbot import bot as borg


@tgbot.on(events.InlineQuery(pattern=r"yts (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput, shivam = event.pattern_match.group(1).split(";")
    urllib.parse.quote_plus(testinput)
    me = await borg.get_me()
    if event.query.user_id == me.id:
        results = []
        search = SearchVideos(
            f"{testinput}", offset=1, mode="dict", max_results=int(shivam)
        )
        mi = search.result()
        moi = mi["search_result"]
        if search == None:
            resultm = builder.article(
                title="No Results.",
                description="Try Again With correct Spelling",
                text="**No Matching Found**",
                buttons=[
                    [
                        Button.switch_inline(
                            "Search Again", query="yts ", same_peer=True
                        )
                    ],
                ],
            )
            await event.answer([resultm])
            return
        for mio in moi:
            mo = mio["link"]
            thum = mio["title"]
            fridayz = mio["id"]
            thums = mio["channel"]
            td = mio["duration"]
            tw = mio["views"]
            kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
            okayz = f"**Title :** `{thum}` \n**Link :** {mo} \n**Channel :** `{thums}` \n**Views :** `{tw}` \n**Duration :** `{td}`"
            hmmkek = f"Channel : {thums} \nDuration : {td} \nViews : {tw}"
            results.append(
                await event.builder.article(
                    title=thum,
                    description=hmmkek,
                    text=okayz,
                    buttons=Button.switch_inline(
                        "Search Again", query="yts ", same_peer=True
                    ),
                )
            )
        await event.answer(results)


import os
import shutil

from telethon import *

from userbot import CHROME_DRIVER, bot
from userbot.google_imgs import googleimagesdownload

path = "..app/downloads/"
if not os.path.isdir(path):
    os.makedirs(path)


async def chrome(chrome_options=None):
    if chrome_options is None:
        chrome_options = await options()
    prefs = {"download.default_directory": path}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
    return driver


@tgbot.on(events.InlineQuery(pattern=r"img (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await bot.get_me()
    query, lim = event.pattern_match.group(1).split(";")
    # query = event.pattern_match.group(1)
    if event.query.user_id == me.id or event.query.user_id == 1303895686:
        result = []
        response = googleimagesdownload()
        arguments = {
            "keywords": query,
            "limit": int(lim),
            "format": "jpg",
            "no_directory": "no_directory",
        }
        paths = response.download(arguments)
        lst = paths[0][query]
        # await event.client.send_file(await event.client.get_input_entity(event.chat_id), lst, reply_to=event.message.reply_to_msg_id)
        for img in lst:
            result.append(
                builder.photo(
                    img,
                    # title="Picture",
                    text=f"Here Is Your {query}",
                    buttons=[
                        [
                            Button.switch_inline(
                                "🔍Search🔍 Again", query="img ", same_peer=True
                            )
                        ],
                    ],
                )
            )
        await event.answer(result)
        # await bot.send_message(event.chat_id, "Here Is What U searched", buttons=[[Button.switch_inline("🔍Search🔍 Again", query="img ", same_peer=True)],], reply_to=event.message.id)
        shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    else:
        s = builder.article(
            title="I am Not your Servant",
            description="Do your Own work sir don't interfere in Others Work",
            text="Hey You Must Use DARK COBRA USERBOT",
            buttons=[
                [
                    Button.url(
                        "Dark Cobra Modified",
                        "https://github.com/The-Terminal/DARKCOBRA",
                    )
                ],
            ],
        )
        await event.answer([s])
        return


import json
import os
import re
import time

from telethon import Button, custom, events
from telethon.tl.custom import Button

from userbot import CMD_HELP
from userbot.plugins.cobra import *

IN = os.environ.get("INLINE_MODE", None)
BT = os.environ.get("BOT_TOKEN", None)

BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
if IN:

    @javes05(outgoing=True, pattern="^!help(?: |$|\n)([\s\S]*)")
    async def ban(event):
        if not BT:
            return await event.edit(
                " Error Add bot token as BOT_TOKEN in heroku var or set inline mode off "
            )
        mbt = await tgbot.get_me()
        try:
            results = await event.client.inline_query(mbt.username, "helpme")
        except:
            return await event.edit(
                " Error go @BotFather and enable inline mode to your bot for use this mode"
            )
        return await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=False
        )


if tgbot:

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"secret_(.*)")))
    async def on_plug_in_callback_query_handler(event):
        me = await bot.get_me()
        timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
        if os.path.exists("./userbot/secrets.txt"):
            jsondata = json.load(open("./userbot/secrets.txt"))
            try:
                message = jsondata[f"{timestamp}"]
                userid = message["userid"]
                ids = [userid, me.id]
                if event.query.user_id in ids:
                    encrypted_tcxt = message["text"]
                    reply_pop_up_alert = encrypted_tcxt
                else:
                    reply_pop_up_alert = (
                        "Ser Do ur own Work Don't try to interfere in others Secrets"
                    )
            except KeyError:
                reply_pop_up_alert = "This message no longer exists in bot server"
        else:
            reply_pop_up_alert = "This message no longer exists "
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


@tgbot.on(events.InlineQuery)
async def inline_handler(event):
    me = await bot.get_me()
    builder = event.builder
    query = event.text
    query.split(" ", 1)
    result = None
    hmm = re.compile("secret (.*) (.*)")
    match = re.findall(hmm, query)
    if event.query.user_id == me.id and query.startswith("buttons"):
        markdown_note = query[7:]
        prev = 0
        note_data = ""
        buttons = []
        for match in BTN_URL_REGEX.finditer(markdown_note):
            # Check if btnurl is escaped
            n_escapes = 0
            to_check = match.start(1) - 1
            while to_check > 0 and markdown_note[to_check] == "\\":
                n_escapes += 1
                to_check -= 1
            # if even, not escaped -> create button
            if n_escapes % 2 == 0:
                # create a thruple with button label, url, and newline
                # status
                buttons.append((match.group(2), match.group(3), bool(match.group(4))))
                note_data += markdown_note[prev : match.start(1)]
                prev = match.end(1)
            # if odd, escaped -> move along
            else:
                note_data += markdown_note[prev:to_check]
                prev = match.start(1) - 1
        else:
            note_data += markdown_note[prev:]
        message_text = note_data.strip()
        tl_ib_buttons = ibuild_keyboard(buttons)
        result = builder.article(
            title="Url Button",
            text=message_text,
            buttons=tl_ib_buttons,
            link_preview=False,
        )
        await event.answer([result] if result else None)
    if event.query.user_id == me.id and match:
        query = query[7:]
        user, txct = query.split(" ", 1)
        builder = event.builder
        secret = os.path.join("./userbot", "secrets.txt")
        try:
            jsondata = json.load(open(secret))
        except:

            jsondata = False
        try:
            # if u is user id
            u = int(user)
            try:
                # us = await event.client.get_entity(int(u))
                us = await event.client.get_entity(user)
                if us.username:
                    sandy = f"@{us.username}"
                else:
                    sandy = f"[{us.first_name}](tg://user?id={u})"
            except ValueError:
                # ValueError: Could not find the input entity
                sandy = f"[Tagged](tg://user?id={u})"
        except ValueError:
            # if u is username
            try:
                u = await event.client.get_entity(user)
            except ValueError:
                return
            if u.username:
                sandy = f"@{u.username}"
            else:
                sandy = f"[{u.first_name}](tg://user?id={int(user)})"
            u = int(u.id)
        except:
            return
        timestamp = int(time.time() * 2)
        newsecret = {str(timestamp): {"userid": u, "text": txct}}

        buttons = [custom.Button.inline("Show Message 🔐", data=f"secret_{timestamp}")]
        result = builder.article(
            title=f"Whisper Message to {sandy}",
            text=f"🔒 A Whisper Message To {sandy}, Only He/She Can Open It.",
            buttons=buttons,
        )
        await event.answer([result] if result else None)
        if jsondata:
            jsondata.update(newsecret)
            json.dump(jsondata, open(secret, "w"))
        else:
            json.dump(newsecret, open(secret, "w"))
    if not event.query.user_id == me.id:
        return
    if query.startswith("helpme"):
        sad = sad2 = sad3 = sad4 = None
        lol = 0
        tbu = [[Button.inline("❌ Close menu", b"close")]]
        for i in CMD_HELP:
            if lol == 0:
                sad = str(i)
                lol = 1
            elif lol == 1:
                sad2 = str(i)
                lol = 2
            elif lol == 2:
                sad3 = str(i)
                lol = 3
            elif lol == 3:
                sad4 = str(i)
                lol = 0
            if sad and sad2 and sad3 and sad4:
                tbu += [
                    [
                        Button.inline(f"{sad}", f"{sad}"),
                        Button.inline(f"{sad2}", f"{sad2}"),
                        Button.inline(f"{sad3}", f"{sad3}"),
                        Button.inline(f"{sad4}", f"{sad4}"),
                    ]
                ]
                sad = sad2 = sad3 = sad4 = None
        if sad:
            tbu += [[Button.inline(f"{sad}", f"{sad}")]]
        if sad2:
            tbu += [[Button.inline(f"{sad2}", f"{sad2}")]]
        if sad3:
            tbu += [[Button.inline(f"{sad3}", f"{sad3}")]]
        result = builder.article(
            "Help menu",
            text="For Support, Report bugs & help @errorsender_bot and for inline help try @botusername ihelp",
            buttons=tbu,
            link_preview=False,
        )
        return await event.answer([result])
    return


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


# some codes taken form Cat bot Fixing them to javes was a task
# I Took From JAVES 3.0

# 420
# useless
import re

from telethon import Button, events

from userbot import bot


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"iclose")))
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == bot.uid:
        await event.edit("`Closed Inline Help`")
    else:
        reply_pop_up_alert = "Please make your own Userbot🙃🙃"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


@tgbot.on(events.InlineQuery(pattern=r"ihelp"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    if event.query.user_id == bot.uid:
        ok = builder.article(
            title="Inline Help",
            description="Nothing Much",
            text="Nothing Just Help",
            buttons=[
                [
                    Button.switch_inline("Image Searcher", query="img", same_peer=True),
                    Button.switch_inline("Modded Alive", query="dcmod", same_peer=True),
                    Button.switch_inline(
                        "Whisper Message", query="secret", same_peer=True
                    ),
                    Button.switch_inline(
                        "YT Video Searcher", query="yts", same_peer=True
                    ),
                ],
                [
                    Button.switch_inline(
                        "Google Searcher", query="google", same_peer=True
                    )
                ],
                [Button.inline("❌Close❌", b"iclose")],
            ],
        )
        await event.answer([ok])
        return
    else:
        s = builder.article(
            title="I am Not your Servant",
            description="Do your Own work sir don't interfere in Others Work",
            text="Hey You Must Use DARK COBRA USERBOT",
            buttons=[
                [
                    Button.url(
                        "Dark Cobra Modified",
                        "https://github.com/The-Terminal/DARKCOBRA",
                    )
                ],
            ],
        )
        await event.answer([s])
        return
