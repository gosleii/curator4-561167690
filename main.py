import telebot
import random

la_liga = ["Алавес", "Атлетик Бильбао", "Атлетико Мадрид", "Барселона", "Сельта", "Эспаньол", "Хетафе", "Жирона", "Лас-Пальмас", "Леганес", "Мальорка", "Осасуна", "Райо Вальекано", "Реал Бетис", "Реал Мадрид", "Реал Сосьедад", "Вальядолид", "Севилья", "Валенсия", "Вильярреал"]

rpl = ["Зенит", "Динамо", "ЦСКА", "Локомотив", "Спартак", "Химки", "Оренбург", "Ростов", "Рубин", "Акрон", "Пари НН", "Краснодар", "Динамо Махачкала", "Ахмат", "Факел", "Крылья Советов"]

bot = telebot.TeleBot('7319417540:AAGNv-9IMQzkJHMieyNJRRXnkj7HdQoKTf4')

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['random_laliga_team'])
def random_laliga_team_handler(message):
    bot.send_message(message.chat.id, text=random.choice(la_liga), parse_mode="Markdown")

@bot.message_handler(commands=['zenit'])
def zenit_handler(message):
    bot.send_message(message.chat.id, text='[Зенит](https://ru.m.wikipedia.org/wiki/Зенит_(футбольный_клуб,_Санкт-Петербург)', parse_mode="Markdown")

@bot.message_handler(commands=['random_rpl_team'])
def random_rpl_team_handler(message):
    bot.send_message(message.chat.id, text=random.choice(rpl), parse_mode="Markdown")

bot.infinity_polling()