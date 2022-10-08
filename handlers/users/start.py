from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from datetime import datetime

from loader import dp, db, bot
import sqlite3

@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
	name = message.from_user.full_name
	today = datetime.now().date()
	try:
		db.add_user(id=message.from_user.id,
                    name=name, 
                    date_of_start=today,
                    check_sub=0)
		# await bot.send_message(GROUP_CHAT_ID, f"{name} start bosdi.\nid:<a href='tg://user?id={message.from_user.id}'> {message.from_user.id} </a>")
	except sqlite3.IntegrityError as err:
		pass
	await message.answer(f"Salom, {message.from_user.full_name}! ")
	# await message.answer(f"Mintaqani tanlang",reply_markup=shahar_btn_yasash(shaharlar_data))
