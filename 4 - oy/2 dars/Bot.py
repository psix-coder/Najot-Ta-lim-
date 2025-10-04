from telebot import TeleBot
from telebot.types import Message

bot = TeleBot("8154458815:AAGRlIxDQmCPNXbgTZMpd7W85Q-GJleEF6Y")

@bot.message_handler(commands=["start"])
def reaction_to_start(message: Message):
    chat_id = message.chat.id  # Bu yerda to'g'ri chat ID ni olish kerak
    print(message.chat.type)
    bot.send_message(chat_id=chat_id, text="Salom, nma gap!")  # chat_id parametrini to'g'ri berish

# Botni ishga tushirish
bot.infinity_polling()
