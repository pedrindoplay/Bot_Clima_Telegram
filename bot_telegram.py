import os
import telebot
from api import Clima
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda m: m.text and m.text.startswith('/'))
def temperatura(message):
    cidade = message.text
    cidade = cidade.replace("/", "")
    try:
        tempo, pressao, temperatura, umidade = Clima(cidade)
        bot.reply_to(message, f"Em {cidade}\nO tempo está com {tempo}\nA pressão atmosferica é de {pressao}\nEstá fazendo {temperatura}° graus\nE a umidade é de {umidade}")
    except:
        bot.reply_to(message, "aconteceu um erro, tente digitar novamente")



@bot.message_handler(func=lambda msg:True)
def bemvindo(mensage):
    bot.reply_to(mensage, "Olá! Sou o Bot de Clima, para consultar o clima da sua cidade, ou de qualquer outra, basta digitar '/' e o nome da sua cidade.")


bot.infinity_polling()