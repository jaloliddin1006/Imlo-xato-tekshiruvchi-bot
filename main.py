from uzwords import words
from difflib import get_close_matches


def checkWord(word, words=words):
	word = word.lower()
	matches = set(get_close_matches(word, words, n=4))
	available = False
	print(matches)

	if word in matches:
		available = True
		matches = word
	elif 'х' in word:
		word = word.replace('х', 'ҳ')
		matches.update(get_close_matches(word, words))
	elif 'ҳ' in word:
		word = word.replace('ҳ', 'х')
		matches.update(get_close_matches(word, words))

	return {'available':available, 'matches':matches}

# if __name__=='__main__':
# 	result = (checkWord("мактуб"))
# 	# print(checkWord('мактуб'))
# 	# print(checkWord('salom'))
# 	print(result['available'])
# 	for text in result['matches']:
# 		print(f"{text.capitalize()}\n")
		