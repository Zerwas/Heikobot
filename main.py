import sys
import os
import time
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
from datetime import datetime
import json
from pprint import pprint
import random

def getScriptPath():
        return os.path.dirname(os.path.realpath(sys.argv[0]))

scriptPath = getScriptPath()

TOKEN = sys.argv[1]
bot = telepot.Bot(TOKEN)

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print("Got a new message: ")
	pprint(msg)

	responses = [\
	"Gute Idee, aber kann man das auch mit Bigrammen lösen? \n\n _Said under various locations and circumstances_", \
	"Na Algorithmen und Datenstrukturen! \n\n _When entering rooms_",
	"Das ... Das kann ich Ihnen jetzt grade nicht beantworten. Kommen sie bitte nach der Vorlesung nochmal nach vorne. \n\n _When caught off guard_"]
	if msg['text'][:6] == "/zitat":
		bot.sendMessage(chat_id, random.choice(responses), parse_mode="Markdown")

	haiku = "In the Arctic ring,\n\
	An ancient tree is derived.\n\
	How much does it weigh? "
	if msg['text'][:6] == "/haiku":
		bot.sendMessage(chat_id, haiku, parse_mode="Markdown")
	
	about = "Find me here: https://github.com/offensivebots/Heikobot"

	if msg['text'][:6] == "/about":
		bot.sendMessage(chat_id, about, parse_mode="Markdown")

bot.message_loop({'chat': on_chat_message})
print('Listening ...')

while 1:
	time.sleep(60)