from create_bot import bot
from telebot import types

def country(message):
    global Country
    Country = message.text
    msg = bot.send_message(message.chat.id, f'Вы выбрали <b>-Купить недвижимость за границей</b>\nCтрана: <b>{Country}</b>\n\nВведите название города', parse_mode='html')
    bot.register_next_step_handler(msg, sity)

def sity(message):
    global Sity
    Sity = message.text
    
    markupGranBuy = types.InlineKeyboardMarkup()

    item_granBuyKvart = types.InlineKeyboardButton(text='Квартира', callback_data='granBuyKvart')
    item_granBuyHome = types.InlineKeyboardButton(text='Дом', callback_data = 'granBuyHome')
    item_granBuyKomm = types.InlineKeyboardButton(text='Коммерция', callback_data='granBuyKomm')
    item_backGranBuy = types.InlineKeyboardButton(text='Вернуться на шаг назад', callback_data='backGranBuy')

    markupGranBuy.add(item_granBuyKvart, item_granBuyHome)
    markupGranBuy.add(item_granBuyKomm)
    markupGranBuy.add(item_backGranBuy)

    bot.send_message(message.chat.id, f'-Купить недвижимость за границей\n\nСтрана: {Country}\nГород: {Sity}', reply_markup=markupGranBuy)

def countrySell(message):
    global CountrySell
    CountrySell = message.text
    msg = bot.send_message(message.chat.id, f'Вы выбрали <b>-Продать недвижимость за границей</b>\nCтрана: <b>{CountrySell}</b>\n\nВведите название города', parse_mode='html')
    bot.register_next_step_handler(msg, sitySell)

def sitySell(message):
    global SitySell
    SitySell = message.text

    markupGranSell = types.InlineKeyboardMarkup()

    item_granSellKvart = types.InlineKeyboardButton(text='Квартира', callback_data='granSellKvart')
    item_granSellHome = types.InlineKeyboardButton(text='Дом', callback_data = 'granSellHome')
    item_granSellKomm = types.InlineKeyboardButton(text='Коммерция', callback_data='granSellKomm')
    item_backGranSell = types.InlineKeyboardButton(text='Вернуться на шаг назад', callback_data='backGranBuy')

    markupGranSell.add(item_granSellKvart, item_granSellHome)
    markupGranSell.add(item_granSellKomm)
    markupGranSell.add(item_backGranSell)

    bot.send_message(message.chat.id, f'-Продать недвижимость за границей\n\nСтрана: {CountrySell}\nГород: {SitySell}', reply_markup=markupGranSell)