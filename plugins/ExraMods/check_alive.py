import time
import random
from pyrogram import Client, filters
from info import BOT_START_TIME, ADMINS

CMD = ["/", "."]


@Client.on_message(filters.command("ping", CMD) & filters.user(ADMINS))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
