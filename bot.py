# import telebot
# import setings

# bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.send_message(message.chat.id, "Эй, Дебил? Работает?")

# if __name__ == "__main__":
#     bot.polling(none_stop=True)