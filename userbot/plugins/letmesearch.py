"""
Let me Google / YouTube / DuckDuckGo / altnews / Xvideo / Pornhub / var / log / dyno that for you! 
Syntax:
 .lmg <search query>
 .lmy <search query>
 .ddg <search query>
 .lmalt <search news>
 .lmx <search porn>
 .lmx2 <search porn>
 .lmp <search porn>
 .lmvar <heroku app name>
 .lmlog <heroku app name>
 .dyno <type billing>
 .lmkp <type name of place as on indiankanoon.com>
 .lmki <Type name of item as on indiankanoon.com>
 .gem <Type name of item as on gem.gov.in>
 .archive <Type name of website you want to get info on wayback machine>
"""


import requests

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="lmg (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=http://google.com/search?q={input_str.replace(" ", "+")}'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me **Googal** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmy (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://www.youtube.com/results?search_query={input_str.replace(" ", "+")}'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me **UThoob** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="ddg (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://duckduckgo.com/?q={input_str.replace(" ", "+")}&t=h_&ia=about'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me **duckduckgo** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmalt (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://www.altnews.in/?s={input_str.replace(" ", "+")}'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me **altnews** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmvar (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://dashboard.heroku.com/apps/{input_str.replace(" ", "+")}/settings'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me **var** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmlog (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://dashboard.heroku.com/apps/{input_str.replace(" ", "+")}/logs'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me **log** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="dyno(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://dashboard.heroku.com/account/{input_str.replace(" ", "+")}'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me **dyno** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmkp (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://indiankanoon.org/search/?formInput={input_str.replace(" ", "+")}+sortby%3Amostrecent'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me **Indiankanoon.com : Place** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="gem (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://mkp.gem.gov.in/search?q={input_str.replace(" ", "+")}&sort_type=created_at_desc&_xhr=1'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me **gem.gov.in** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="archive (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://web.archive.org/web/*/{input_str.replace(" ", "+")}'

    if response_api := requests.get(sample_url).text:
        await event.edit(
            "Let me run your link on wayback machine that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("Something went wrong. Please try again later.")
