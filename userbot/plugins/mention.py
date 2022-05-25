# For Uniborg
# (c) @INF1N17Y

from uniborg.util import admin_cmd


@borg.on(admin_cmd("mention (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = previous_message.forward.sender_id
        else:
            replied_user = previous_message.sender_id
    else:
        await event.edit("reply To Message")
    user_id = replied_user
    caption = f"""<a href='tg://user?id={user_id}'>{input_str}</a>"""
    await event.edit(caption, parse_mode="HTML")
