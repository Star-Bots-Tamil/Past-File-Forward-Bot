import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import FloodWait
from config import Config
from translation import Translation

FROM = Config.FROM_CHANNEL
TO = Config.TO_CHANNEL
FILTER = Config.FILTER_TYPE

@Client.on_message(filters.private & filters.command(["forward"]))
async def run(bot, message):
    if str(message.from_user.id) not in Config.OWNER_ID:
        return
        files_count += 1
        await asyncio.sleep(1)        
    buttons = [[
        InlineKeyboardButton('🚫 Stop', callback_data='stop_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    m = await bot.send_message(
        text="<b>File Forwording Started😉\nForwarded Files :- <code>{files_count}</code> Files</b>",
        reply_markup=reply_markup,
        chat_id=message.chat.id
    )

    async for message in bot.USER.search_messages(chat_id=FROM,offset=Config.SKIP_NO,limit=Config.LIMIT,filter=FILTER):
        try:
            if message.video:
                file_name = message.video.file_name
            elif message.document:
                file_name = message.document.file_name
            elif message.audio:
                file_name = message.audio.file_name
            else:
                file_name = None
            await bot.copy_message(
                chat_id=TO,
                from_chat_id=FROM,
                parse_mode=enums.ParseMode.HTML,       
                caption=Translation.CAPTION.format(file_name),
                message_id=message.id
            )
            files_count += 1
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await bot.copy_message(
                chat_id=TO,
                from_chat_id=FROM,
                parse_mode=enums.ParseMode.HTML,       
                caption=Translation.CAPTION.format(file_name),
                message_id=message.id
            )
            files_count += 1
            await asyncio.sleep(1)
        except Exception as e:
            print(e)
            pass
   # await m.delete()
    buttons = [[
        InlineKeyboardButton('📜 Support Group', url='https://t.me/trtechguide')
    ]] 
    reply_markup = InlineKeyboardMarkup(buttons)
    await m.edit(
        text=f"<u><b>Successfully Forwarded</b></u>\n\n<b>Total Forwarded Files :-</b> <code>{files_count}</code> <b>Files</b>\n<b>Thanks For Using Me❤️</b>",
        reply_markup=reply_markup
    )
        
