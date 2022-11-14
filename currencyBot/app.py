import telebot
from config import TOKEN, keys
import extensions

bot = telebot.TeleBot(TOKEN)
 
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    text = "введите команду в формате :\n <имя валюты>  \
\n<в какую валюту перевести> \
\n<сколько валюты перевести> \
\n либо введите values чтобы увидеть список доступных валют" 
    bot.reply_to(message, text)

@bot.message_handler(commands= ['values'])
def function_name(message: telebot.types.Message):
    text = 'Доступные вылюты'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    text = ''
    values = message.text.split(' ')
    if len(values) != 3:
        text = 'вы ввели неверное количество параметров'
    else:    
        text = extensions.CryptoConverter.convertExceptions(values)
        if not text:
            quote, base, amount = values
            result = extensions.Converter.get_price(quote, base, amount)
            text = f'Цена {amount} {quote} в {base} - {result}'
            
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)