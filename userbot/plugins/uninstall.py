import os

from userbot.events import remove_plugin
from userbot.utils import admin_cmd, remove_plugin, sudo_cmd


@bot.on(admin_cmd(pattern=r"uninstall (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"uninstall (?P<shortname>\w+)", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path = f"./userbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"Uninstalled {shortname} successfully By Dark Cobra")
    except OSError as e:
        await event.edit("Error: %s : %s" % (dir_path, e.strerror))


# BY SHIVAM
# TEAM DC
