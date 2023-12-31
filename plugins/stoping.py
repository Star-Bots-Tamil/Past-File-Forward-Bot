import os
import sys
import asyncio
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

@Client.on_callback_query(filters.regex(r'^stop_btn$'))
async def stop_button(c: Client, cb: CallbackQuery):
    files_count = 0
    await cb.message.delete()
    await cb.answer()
    msg = await c.send_message(
        text="<i>Trying To Stopping.....</i>",
        chat_id=cb.message.chat.id
    )
    await asyncio.sleep(5)
    await msg.edit("<b><i>File Forword Stopped Successfully 👍🏻</i>\nTotal Forwarded Files :- <code>{files_count}</code> Files</b>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close(bot, update):
    await update.answer()
    await update.message.delete()
