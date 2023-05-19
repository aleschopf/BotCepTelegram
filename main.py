from consultar_cep import consultar_cep
from dotenv import load_dotenv 
import telebot
import os

load_dotenv()

CHAVE_API = os.getenv("API_KEY")

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Envie o número do CEP para receber o endereço referente a ele.")

@bot.message_handler()
def cep(message):
    resultado = consultar_cep(message.text)
    mensagem = resultado
    bot.send_message(message.chat.id, mensagem)

bot.infinity_polling()