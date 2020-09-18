import telebot

bot = telebot.TeleBot("1342433720:AAHz-6NJz4tWCF2_cdQdKlxjXZGI_xTRx6E", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Эй, Дебил? Работает?")

if __name__ == "__main__":
    bot.polling(none_stop=True)