import logging

from aiogram import Bot, Dispatcher, executor, types
from main import checkWord
from translate import to_latin, to_cyrillic

API_TOKEN = '5064903241:AAGVUTebNRCdaLH5lrVcRp9SiHlPnFpSQn4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token = API_TOKEN)
dp =Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
	await message.reply('uz-imlo botiga xush kelibsiz!')


@dp.message_handler(commands='help')
async def help_user(message: types.Message):
	await message.reply('botdan foydalanish uchun so\'z yuboring')

@dp.message_handler()
async def check_Imlo(message: types.Message):
	words = message.text.split()
	for word in words:
		word1 = word
		matn = word
  ###########################################################################################
  ###########################################################################################
      
      
		if matn.isascii():
      
    
		    word1 = to_cyrillic(matn)
		# else:
		#     word = to_latin(matn)
  ###########################################################################################
  ###########################################################################################


		result = checkWord(word1)
		if result['available']:
			if word.isascii():
				response = f"✅ {to_latin(word1).capitalize()}"
			else:
				response = f"✅ {word1.capitalize()}"


		else:
			if word.isascii():
				response = f"❌ {to_latin(word).capitalize()}\n"
				for text in result['matches']:
					response += f"✅ {to_latin(text).capitalize()}\n"
			else:
				response = f"❌ {word.capitalize()}\n"
				for text in result['matches']:
					response += f"✅ {text.capitalize()}\n"

		await message.answer(response)

if __name__=='__main__':
	executor.start_polling(dp, skip_updates=True)