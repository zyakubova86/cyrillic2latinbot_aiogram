# from io import BytesIO
#
# import telebot
# from telebot import types
# from transliterate import to_latin, to_cyrillic
# import qrcode
#
# TOKEN = ""
# bot = telebot.TeleBot(TOKEN, parse_mode=None)


# commands
# start - Starts the bot
# qr - Generates qr code from text

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     reply = f"Assalom alaykum. {bot.get_me()} xush kelibsiz!"
#     reply += "\nMatn kiriting"
#     bot.reply_to(message, reply)


# @bot.message_handler(func=lambda message: True)
# def cyrillic2latin(message):
#     bot.send_message(message.chat.id, 'Insert text to transliterate to cyriilic or visa-verse')
#
#     user_message = message.text
#     bot_reply = lambda user_message: to_cyrillic(user_message) if user_message.isascii() else to_latin(user_message)
#     # if user_message.isascii():
#     #     bot_reply = to_cyrillic(user_message)
#     # else:
#     #     bot_reply = to_latin(user_message)
#     bot.reply_to(message, bot_reply(user_message))


# @bot.message_handler(commands=['qr'])
# def creating_qr(message):
#     bot.send_message(message.chat.id, 'QR kodga aylantirish uchun url ni kiriting')
#
#     @bot.message_handler(content_types=['text'])
#     def creating_qr(message):
#         qr_img = qrcode.make(message.text)
#         bio = BytesIO()
#         qr_img.save(bio, 'JPEG')
#         bio.seek(0)
#         bot.send_photo(message.chat.id, bio)
#
#
# bot.infinity_polling()
