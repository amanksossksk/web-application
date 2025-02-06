
from telebot import *

bot = telebot.TeleBot("7274261029:AAFKTqs4mwUZ6xCv29UIOLItvXt7fPvXMh0")
@bot.message_handler(commands=['start'])
def start(message):
 bot.reply_to(message,parse_mode='HTML',text = (f"<b>Hello -> </b><i>{message.from_user.first_name}</i> ðŸ˜€\n<b>USER ID -> </b><i>{message.from_user.id} ðŸ¤–</i>\n<b>TO CHECK MY MENU SEND -> </b><i>/cmds</i>"))
