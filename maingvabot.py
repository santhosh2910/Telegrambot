from telegram import*
from telegram.ext import*
from requests import *

updater=Updater(token="5075504450:AAFzR7vDxz54GLyFE7WASjAq897_v4X6m58")
dispatcher = updater.dispatcher

def startCommand(update:Update,context:CallbackContext):
    buttons=[[KeyboardButton("Dictionary")],[KeyboardButton("Social Media")]]
    context.bot.send_message(chat_id=update.effective_chat.id,text="Welcome to my bot!",
    reply_markup=ReplyKeyboardMarkup(buttons))

 

dispatcher.add_handler(CommandHandler("start",startCommand))

updater.start_polling()
