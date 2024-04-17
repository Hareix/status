import asyncio
from sys import version as pyver

import pyrogram, uvloop
from pyrogram import __version__ as pyrover
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import Message

import config

uvloop.install()
loop = asyncio.get_event_loop()
SUDO_USERS = config.SUDO_USER
ADMIN_USERS = config.ADMIN_USER

app2 = pyrogram.Client(
    ":YukkiBot:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

save = {}
grouplist = 1


async def init():
    await app2.start()

    @app2.on_message(filters.command(["start", "help"]) & filters.private)
    async def start_command(_, message: Message):
        await message.reply_text(config.PRIVATE_START_MESSAGE)

    @app2.on_message(filters.private)
    async def incoming_private(_, message):
        user_id = message.from_user.id
        if user_id in ADMIN_USERS:
            if message.reply_to_message:
                replied_id = message.reply_to_message.id
                try:
                    replied_user_id = save[replied_id]
                except Exception as e:
                    print(e)
                    return await message.reply_text(
                        "Failed to fetch user. You might've restarted bot or some error happened. Please check logs"
                    )
                try:
                    return await app2.copy_message(
                        replied_user_id,
                        message.chat.id,
                        message.id,
                    )
                except Exception as e:
                    print(e)
                    return await message.reply_text(
                        "Failed to send the message, User might have blocked the bot or something wrong happened. Please check logs"
                    )
                    
        else:
           	for user in SUDO_USERS:
                    try:
                        forwarded = await app2.forward_messages(
                            user, message.chat.id, message.id
                        )
                        save[forwarded.id] = user_id
                    except:
                        pass
           	

    print("[LOG] - Yukki Chat Bot Started")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
