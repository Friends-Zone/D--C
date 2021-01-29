# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot plugin_info command """

from userbot import CMD_HELP
from userbot.utils import admin_cmd, sudo_cmd, CmdHelp, edit_or_reply


@borg.on(admin_cmd(outgoing=True, pattern="plinfo(?: |$)(.*)"))
@borg.on(sudo_cmd(allow_sudo=True, pattern="plinfo(?: |$)(.*)"))
async def info(event):
    """ For .plinfo command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CmdHelp:
            await edit_or_reply(event, str(CmdHelp[args]))
        else:
            await edit_or_reply(event,  "Maybe the command help or plugin info has not been set or the plugin is invalid..."
            )
    else:
        await edit_or_reply(event,  "Please specify which plugin do you want help for !!\
            \nUsage: .pinfo <plugin name>"
        )
        string = ""
        for i in CmdHelp:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
