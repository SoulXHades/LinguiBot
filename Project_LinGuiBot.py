import sys      #sys-system-specific parameters and functions
import time
import telepot
from telepot.loop import MessageLoop
from google.cloud import translate # Imports the Google Cloud client library
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
from GCloudLangList import langList
from LinguiBotInlineKeyboard import inLineKeyboardDict
from LinguiBotDicts import PreviewMessage
from LinguiBotDicts import CallBackList

#define inLine Dictionary for edit of messages
inLineDict = {}
#define Dictionary for Default Target language
DefaultLang = {}

#This function handles the commands sent by either inLine buttons or chat
def handle_commands(chat_id, commands, msgType):

	if commands == 'start':
		#try except is useful when server restarted and user clicked on previous inLine buttons
		try:
			if msgType == 'inLine':
				#Edit existing text and inline buttons
				inLineDict[chat_id] = bot.editMessageText(telepot.message_identifier(inLineDict[chat_id]), \
					text=PreviewMessage['mainmenu'], reply_markup=inLineKeyboardDict['about_help_targetlang'])
				return
		except KeyError:
			print(chat_id, "KeyError. \nFixed by resending new message.")

		#Obtain the 'start' message from LinguiBotDicts.py to send to user
		bot.sendMessage(chat_id, PreviewMessage['start'])

		#Obtain the 'mainmenu' message from LinguiBotDicts.py to send to user
		#Sends a fresh new text and inline buttons
		inLineDict[chat_id] = bot.sendMessage(chat_id, PreviewMessage['mainmenu'], reply_markup=inLineKeyboardDict['about_help_targetlang'])

	elif commands == 'about':
		#try except is useful when server restarted and user clicked on previous inLine buttons
		try:
			if msgType == 'inLine':
				#Edit existing text and inline buttons
				inLineDict[chat_id] = bot.editMessageText(telepot.message_identifier(inLineDict[chat_id]), \
					text=PreviewMessage['about'], reply_markup=inLineKeyboardDict['mainmenu'])
				return
		except KeyError:
			print(chat_id, "KeyError. \nFixed by resending new message.")

		#Obtain the 'about' message from LinguiBotDicts.py to send to user
		#Sends a fresh new text and inline buttons
		inLineDict[chat_id] = bot.sendMessage(chat_id, PreviewMessage['about'], reply_markup=inLineKeyboardDict['mainmenu'])

	elif commands == 'langlists':
		bot.sendMessage(chat_id, PreviewMessage['langlists'])

	elif commands == 'targetlang':
		#try except is useful when server restarted and user clicked on previous inLine buttons
		try:
			if msgType == 'inLine':
				#Edit existing text and inline buttons
				inLineDict[chat_id] = bot.editMessageText(telepot.message_identifier(inLineDict[chat_id]), \
					text=PreviewMessage['targetlang'], reply_markup=inLineKeyboardDict['targetlang'])
				return
		except KeyError:
			print(chat_id, "KeyError. \nFixed by resending new message.")

		#Obtain the 'targetlang' message from LinguiBotDicts.py to send to user
		#Sends a fresh new text and inline buttons
		inLineDict[chat_id] = bot.sendMessage(chat_id, PreviewMessage['targetlang'], reply_markup=inLineKeyboardDict['targetlang'])

	elif commands == 'help':
		#try except is useful when server restarted and user clicked on previous inLine buttons
		try:
			if msgType == 'inLine':
				#Edit existing text and inline buttons
				inLineDict[chat_id] = bot.editMessageText(telepot.message_identifier(inLineDict[chat_id]), \
					text=PreviewMessage['help'], reply_markup=inLineKeyboardDict['mainmenu'])
				return
		except KeyError:
			print(chat_id, "KeyError. \nFixed by resending new message.")

		#Obtain the 'help' message from LinguiBotDicts.py to send to user
		#Sends a fresh new text and inline buttons
		inLineDict[chat_id] = bot.sendMessage(chat_id, PreviewMessage['help'], reply_markup=inLineKeyboardDict['mainmenu'])

	else:
		#Seperate commands and text to be translated
		text = commands.split(' ', 1)

		#For wrong commands or setting of default target language
		try:
			TranslateMessage(chat_id, langList[text[0]], text[1])
		except IndexError:
			#Set the default language for user's future use without using command again
			DefaultLang[chat_id] = langList[text[0]]
			bot.sendMessage(chat_id, "Your default language has been set.")
		except KeyError:
			#When user did not input the right command
			bot.sendMessage(chat_id, "Please input the right command.")

#Set default target language through inLine buttons
def handle_inlineLangLists(chat_id, callBackData):
	#For usability, CallBackList dictionary is obtain from LinguiBotDicts.py
	#callBackData will be compared to the dictionary and execute if it is true
	for callBackDataIndex in range(1, 8):
		if callBackData == CallBackList[callBackDataIndex]:
			#try except is useful when server restarted and user clicked on previous inLine buttons
			try:
				#Edit existing text and inline buttons
				inLineDict[chat_id] = bot.editMessageText(telepot.message_identifier(inLineDict[chat_id]), \
					text=PreviewMessage['targetlang'], reply_markup=inLineKeyboardDict[callBackData])
				return
			except KeyError:
				print(chat_id, "KeyError. \nFixed by resending new message.")
		
			#Sends a fresh new text and inline buttons
			inLineDict[chat_id] = bot.sendMessage(chat_id, PreviewMessage['targetlang'], reply_markup=inLineKeyboardDict[callBackData])
			return

	#for loop is used to convert codes to ASCII A to Z thus reduces code
	for keyboardLetter in range(65, 91):
		#There is no O and Q, hence can skip them
		if keyboardLetter == 79 or keyboardLetter == 81:
			continue

		#chr()+1 to compare callBackData to keys like M1, S1, etc.
		if callBackData == chr(keyboardLetter) or callBackData == (chr(keyboardLetter)+'1') or callBackData == (chr(keyboardLetter)+'2'):
			#try except is useful when server restarted and user clicked on previous inLine buttons
			try:
				#Edit existing text and inline buttons
				inLineDict[chat_id] = bot.editMessageText(telepot.message_identifier(inLineDict[chat_id]), \
					text=PreviewMessage['targetlangSelection'], reply_markup=inLineKeyboardDict[callBackData])
				return
			except KeyError:
				print(chat_id, "KeyError. \nFixed by resending new message.")
		
			#Sends a fresh new text and inline buttons
			inLineDict[chat_id] = bot.sendMessage(chat_id, PreviewMessage['targetlangSelection'], reply_markup=inLineKeyboardDict[callBackData])
			return

#Handles query from inlineKeyboard
def handle_inlineKeyboard(msg):
	#print(msg) #For debugging
	query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

	#This will get the chat_id instead of user's ID
	from_id = msg['message']['chat']['id']

	print("inlinekeyboard: From userid", from_id, query_data)

	#Handles commands from inLine Keyboard
	if query_data.startswith("/"):
		handle_commands(from_id, query_data[1:].lower(), 'inLine')
	else:
		handle_inlineLangLists(from_id, query_data)

    # answer callback query or else telegram will forever wait on this
	bot.answerCallbackQuery(query_id)

#This function is used when users personal message the bot
def on_inline_query(msg):
	#print(msg) #For debugging
	#Obtain data of the message
	query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')

	print('Inline Query:', query_id, from_id, query_string)

	#Define text_translated
	#Translated text will be assigned in this variable
	text_translated = ""

	#Language commands starts with "/"
	if query_string.startswith("/"):
		#Seperate commands and text to be translated
		text = query_string[1:]
		text = text.split(' ', 1)

		#For wrong commands or input method
		try:
			text_translated = TranslateMessage(0, langList[text[0]], text[1])
		except IndexError:
			#Se the default language for user's future use without using command again
			DefaultLang[from_id] = langList[text[0]]
			print("Inline Query: Set default language for user id", from_id)
		except KeyError:
			#When user did not input the right command
			print("Inline Query: Wrong command")
	#To prevent empty string send for translation
	elif len(query_string) > 0:
		try:
			text_translated = TranslateMessage(0, DefaultLang[from_id], query_string)
		except KeyError:
			print("Inline Query: No default target language set. \nUsing English as default target language...")
			text_translated = TranslateMessage(0, langList['eng'], query_string)

	#This will prefers empty message and title from being sent as answer for inline query
	if text_translated == "":
		return

	articles = [InlineQueryResultArticle(
		id='abc',
		title=text_translated,
		input_message_content=InputTextMessageContent(
		message_text=text_translated)
		)]

	bot.answerInlineQuery(query_id, articles)

#Handles normal chat
def handle(msg):
	#print(msg) #For debugging
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	#Return if it is not a text
	if content_type != 'text':
		return

	text = msg['text']

	#Handles commands from normal chat
	if text.startswith("/"):
		#Remove username of bot if query from group chat
		text = text.split('@')
		text = text[0]
		handle_commands(chat_id, text[1:], 'Normal')
		return
	else:
		try:
			TranslateMessage(chat_id, DefaultLang[chat_id], text)
		except KeyError:
			print("No default target language set. \nUsing English as default target language...")
			TranslateMessage(chat_id, langList['eng'], text)

#To Translate Messages
def TranslateMessage(chat_id, target, text):
	translate_client = translate.Client() # Instantiates a client
	translation = translate_client.translate(text, target_language=target)

	#inline query do not have a chat id
	if chat_id != 0:
		bot.sendMessage(chat_id, u'Text: {}'.format(text))
		bot.sendMessage(chat_id, u'Translation: {}'.format(translation['translatedText']))

	return translation['translatedText']
        
bot = telepot.Bot("###TELEGRAM API TOKEN HERE###")
#Async function to look out for incoming messages
MessageLoop(bot, {'chat': handle,
'callback_query': handle_inlineKeyboard, 
'inline_query': on_inline_query}).run_as_thread()
print ('Listening ...')
                  
# Keep the program running.
while 1:
    time.sleep(10)
    