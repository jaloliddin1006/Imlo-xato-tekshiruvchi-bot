from aiogram import executor

from loader import dp, db, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import sqlite3
from data.config import ADMINS


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Ma'lumotlar bazasini yaratamiz:
    # try:
    #     db.create_table_users()
    # except Exception as err:
    #     # pass
    #     print("Error", err)

    # Bot ishga tushgani haqida adminga xabar berish
    try:
        await on_startup_notify(dispatcher)
        
    except Exception as e:
        print(e)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
