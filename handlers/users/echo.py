from aiogram import types

from main import checkWord
from translate import to_latin, to_cyrillic

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
	words = message.text.split()
	for word in words:
		word1 = word
		matn = word
		if matn.isascii():
		    word1 = to_cyrillic(matn)
		# else:
		#     word = to_latin(matn)


		result = checkWord(word1)
		if result['available']:
			print(result)
			if word.isascii():
				response = f"✅ {to_latin(word1).capitalize()}"
			else:
				response = f"✅ {word1.capitalize()}"


		else:
			# print(result)
			# print(result)
			if word.isascii():
				response = f"❌ {to_latin(word).capitalize()}\n"
				for text in result['matches']:
					response += f"✅ {to_latin(text).capitalize()}\n"
			else:
				response = f"❌ {word.capitalize()}\n"
				for text in result['matches']:
					response += f"✅ {text.capitalize()}\n"

		await message.answer(response)
