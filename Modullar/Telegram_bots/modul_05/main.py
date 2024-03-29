from translator_kirilLlatin import to_cyrillic,to_latin
import telebot

TOKEN = "7114673209:AAGtVbxPCmA0rkdgQPO4J8PDMZpgfEJs0tI"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    response = 'Assalomu alaykum?'
    response += '\nKirilchani lotinchaga yoki lotinchani kirilchaga o\'tqizib ko\'ring hohlasyz:'
    bot.reply_to(message,response)

@bot.message_handler(func=lambda message : True)
def echo_all(message):
    text = message.text
    result = lambda text1 : to_cyrillic(text1) if text.isascii() else to_latin(text1)
    bot.reply_to(message, result(text))

bot.polling()
'''
"""
14/01/2021

Dasturlash asoslari

КИРИЛЛ-LOTIN TELEGRAM BOT

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "" #<-- Tokeningizni shu yerga yozing
bot = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f'Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!'
    xabar += '\nMatningizni yuboring.'
    bot.reply_to(message, xabar)

# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))
    

bot.polling()

'''