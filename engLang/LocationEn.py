from create_bot import bot
from telebot import types

def country(message):
    global Country
    Country = message.text
    msg = bot.send_message(message.chat.id, f'You have chosen <b>apartment in another country</b>\nCountry: <b>{Country}</b>\n\nEnter the name of the city', parse_mode='html')
    bot.register_next_step_handler(msg, sity)

def sity(message):    
    global Sity
    Sity = message.text
    
    markupGranBuyEn = types.InlineKeyboardMarkup()

    item_granBuyKvartEn = types.InlineKeyboardButton(text='Apartment', callback_data='granBuyKvartEn')
    item_granBuyHomeEn = types.InlineKeyboardButton(text='House', callback_data = 'granBuyHomeEn')
    item_granBuyKommEn = types.InlineKeyboardButton(text='Commerce', callback_data='granBuyKommEn')
    item_backGranBuyEn = types.InlineKeyboardButton(text='Go back a step', callback_data='backGranBuyEn')

    markupGranBuyEn.add(item_granBuyKvartEn, item_granBuyHomeEn)
    markupGranBuyEn.add(item_granBuyKommEn)
    markupGranBuyEn.add(item_backGranBuyEn)

    bot.send_message(message.chat.id, f'-Buy a property in another country\n\nCountry: {Country}\nCity: {Sity}', reply_markup=markupGranBuyEn)

def countrySell(message):
    global CountrySell
    CountrySell = message.text
    msg = bot.send_message(message.chat.id, f'You have chosen<b>-Sell real estate in another country</b>\nCountry: <b>{CountrySell}</b>\n\nEnter the name of the city', parse_mode='html')
    bot.register_next_step_handler(msg, sitySell)

def sitySell(message):
    global SitySell
    SitySell = message.text

    markupGranSellEn = types.InlineKeyboardMarkup()

    item_granSellKvartEn = types.InlineKeyboardButton(text='Apartment', callback_data='granSellKvartEn')
    item_granSellHomeEn = types.InlineKeyboardButton(text='House', callback_data = 'granSellHomeEn')
    item_granSellKommEn = types.InlineKeyboardButton(text='Commerce', callback_data='granSellKommEn')
    item_backGranSellEn = types.InlineKeyboardButton(text='Go back a step', callback_data='backGranSellEn')

    markupGranSellEn.add(item_granSellKvartEn, item_granSellHomeEn)
    markupGranSellEn.add(item_granSellKommEn)
    markupGranSellEn.add(item_backGranSellEn)

    bot.send_message(message.chat.id, f'-Sell a property in another country\n\nCountry: {CountrySell}\nCity: {SitySell}', reply_markup=markupGranSellEn)