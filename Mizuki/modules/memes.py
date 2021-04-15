import aiohttp
from pyrogram import filters

from Mizuki import pbot


@pbot.on_message(filters.command("memes"))
async def memes(client, message):
    async with aiohttp.ClientSession() as ses:
        async with ses.get("https://some-random-api.ml/meme") as resp:
            r = await resp.json()
            await message.reply_photo(r["image"], caption=r["caption"])


__help__ = """
*Mizuki gives you memes randomly gained through meme API*

• `/memes`*:* get very interesting and funny memes randomly.
"""

__mod_name__ = "Memes"
