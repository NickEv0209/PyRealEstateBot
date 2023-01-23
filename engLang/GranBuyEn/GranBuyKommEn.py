from create_bot import bot
from telebot import types

from engLang import LocationEn

def tel(message):
    global phoneNum
    phoneNum = message.text
    msg2 = bot.send_message(message.chat.id, 'What is your name?')
    bot.register_next_step_handler(msg2, name)

def name(message):
    nMarkUp = types.InlineKeyboardMarkup()
    i_next = types.InlineKeyboardButton(text='Skip', callback_data='nextEn9')
    nMarkUp.add(i_next)

    global Myname
    Myname = message.text
    msg3 = bot.send_message(message.chat.id, 'Enter email\n(Optional)', reply_markup=nMarkUp)
    bot.register_next_step_handler(msg3, email)

def email(message):
    global restMarkupEn
    restMarkupEn = types.InlineKeyboardMarkup()
    item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
    restMarkupEn.add(item_res)

    if '@' in message.text.lower():
        global Myemail
        Myemail = message.text
        bot.send_message('@bottgdb', f'<b>{Myname}</b>\n\n<b>Покупка коммерции за границей</b>\nCтрана: <b>{LocationEn.Country}</b>\nГород: <b>{LocationEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{phoneNum}</b>\neMail: <b>{Myemail}</b>', parse_mode='html')
        bot.send_message(message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)    