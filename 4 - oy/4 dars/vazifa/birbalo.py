"-4552742752"
from telebot import TeleBot
from telebot.types import Message

bot = TeleBot("8154458815:AAGRlIxDQmCPNXbgTZMpd7W85Q-GJleEF6Y")

@bot.message_handler(commands=["start"])
def reaction_to_start(message: Message):
    chat_id = message.chat.id  
    print(message)
    bot.send_message(chat_id=chat_id, text="Salom, nma gap!") 

@bot.message_handler(content_types=["new_chat_members"])
def reaction_to_new_chat_members(message: Message):
    chat_id = message.chat.id
    full_name = message.new_chat_members[0].full_name
    bot.send_message(chat_id, f'{full_name} saytga xush kelibsiz!')

@bot.message_handler(content_types=["animation", "sticker", "photo", "video", "text", "document"])
def reaction_to_content(message: Message):
    chat_id = message.chat.id

    if message.content_type == 'photo':
        bot.send_photo(chat_id, message.photo[-1].file_id, caption=message.caption)
    elif message.content_type == 'video':
        bot.send_video(chat_id, message.video.file_id, caption=message.caption)
    elif message.content_type == 'document':
        bot.send_document(chat_id, message.document.file_id, caption=message.caption)
    elif message.content_type == 'animation':
        bot.copy_message(chat_id, chat_id, message.message_id)
    elif message.content_type == 'sticker':
        bot.copy_message(chat_id, chat_id, message.message_id)
    elif message.content_type == 'text':
        bot.send_message(chat_id, message.text)

bot.infinity_polling()
