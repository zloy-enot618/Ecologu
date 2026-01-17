import telebot
import os
import random
bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def hi(message):
    with open(r"C:\Users\User\Downloads\hi.jpg", 'rb'):
        bot.reply_to(message, "Привет! \nДавай изучим проблему экологии. \nНапиши /help для того, чтобы увидеть список доступных команд!")


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "one(текстово об проблеме), two(демонстратически о проблеме).")

@bot.message_handler(commands=['one'])
def one(message):
    bot.reply_to(message, "Итоговые последствия экологических проблем, вызванных деятельностью человека, включают ухудшение качества атмосферы, загрязнение водных ресурсов, истощение природных ресурсов и изменение климата. Эти последствия затрагивают не только природу, но и здоровье человека, экономику и социальную стабильность.")

@bot.message_handler(commands=['two'])
def two(message):
    images = os.listdir(r"C:\Users\User\OneDrive\Рабочий стол\Python projects\spiski.py\eco_bot\imgs")
    with open(fr"C:\Users\User\OneDrive\Рабочий стол\Python projects\spiski.py\eco_bot\imgs\{random.choice(images)}", 'rb') as b:
        bot.send_photo(message.chat.id, b)
        bot.reply_to(message, "Последствия экологии!")

@bot.message_handler(func=lambda message:True)
def say(message):
    bot.reply_to(message, "Такой команды нет!")
bot.polling()
