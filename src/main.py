import telebot
from src.IA.quey_data import request_openia

TOKEN = "token bot of telegram"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    answer = request_openia(message.text)
    bot.reply_to(message, answer)

if __name__ == '__main__':
    bot.polling(none_stop=True)