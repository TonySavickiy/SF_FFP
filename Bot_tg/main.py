import telebot

TOKEN = '6413215211:AAGdU6qdLbJiA3r91X_DpdFurcxgRNmkSCE'

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(content_types=['voice',])#декоратор для обработки сообщений(функции, которые будут выполнятся при поступлении команды\сообщения)
def function_name(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Клёво{message.chat.id}")
    
    
@bot.message_handler(commands=['infochat'])
def info_chat(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Параметры данного чата следующие: \n Chat id: {message.chat.id}\n Type chat: {message.chat.type}')
    
@bot.message_handler(commands=['name'])
def namer(message: telebot.types.Message):
    bot.reply_to(message, f'Приветствую тебя {message.chat.username}')
    
    
bot.polling(none_stop=True)