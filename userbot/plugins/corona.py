from covid import Covid

from userbot import CMD_HELP
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="corona (.*)"))
async def _(event):

    covid = Covid()

    data = covid.get_data()

    country = event.pattern_match.group(1)

    country_data = get_country_data(country, data)

    output_text = "".join(
        "`{}`: `{}`\n".format(str(name), str(value))
        for name, value in country_data.items()
    )


    await event.edit(
        "**CoronaVirus Info in {}**:\n\n{}".format(country.capitalize(), output_text)
    )


def get_country_data(country, world):

    return next(
        (
            country_data
            for country_data in world
            if country_data["country"].lower() == country.lower()
        ),
        {"Status": "No information yet about this country!"},
    )


CMD_HELP.update({"corona": ".corona (country name)"})
