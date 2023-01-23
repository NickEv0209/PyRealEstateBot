from create_bot import bot
from telebot import types

def sity(message):
    global Sity
    Sity = message.text
    msg1 = bot.send_message(message.chat.id, f'Вы выбрали <b>дом в России</b> \nв городе: <b>{Sity}</b>\n\nВведите номер телефона', parse_mode='html')
    bot.register_next_step_handler(msg1, tel)

def tel(message):
    global phoneNum
    phoneNum = message.text
    msg2 = bot.send_message(message.chat.id, 'Как к вам обращаться?')
    bot.register_next_step_handler(msg2, name)

def name(message):
    nMarkUp = types.InlineKeyboardMarkup()
    i_next = types.InlineKeyboardButton(text='Пропустить', callback_data='next4')
    nMarkUp.add(i_next)

    global Myname
    Myname = message.text
    msg3 = bot.send_message(message.chat.id, 'Введите email\n(Не обязательно)', reply_markup=nMarkUp)
    bot.register_next_step_handler(msg3, email)

def email(message):
    global restMarkup
    restMarkup = types.InlineKeyboardMarkup()
    item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
    restMarkup.add(item_res)

    if '@' in message.text.lower():
        global Myemail
        Myemail = message.text
        bot.send_message('@bottgdb', f'<b>{Myname}</b>\n\n<b>Продажа дома в России</b>\nГород: <b>{Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{phoneNum}</b>\neMail: <b>{Myemail}</b>', parse_mode='html')
        bot.send_message(message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)