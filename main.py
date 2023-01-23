from create_bot import bot
from telebot import types

    #============================================================================================================
    #-------------------------------------------русские библиотеки-----------------------------------------------
    #============================================================================================================

from rusLang.RusBuy import RusBuyKvart
from rusLang.RusBuy import RusBuyHome
from rusLang.RusBuy import RusBuyKomm
from rusLang.GranBuy import GranBuyKvart
from rusLang.GranBuy import GranBuyHome
from rusLang.GranBuy import GranBuyKomm
from rusLang.RusSell import RusSellKvart
from rusLang.RusSell import RusSellHome
from rusLang.RusSell import RusSellKomm
from rusLang.GranSell import GranSellKvart
from rusLang.GranSell import GranSellHome
from rusLang.GranSell import GranSellKomm
from rusLang.BackCall import BackCall

from rusLang import Location

    #============================================================================================================
    #------------------------------------------английские библиотеки---------------------------------------------
    #============================================================================================================

from engLang.RusBuyEn import RusBuyKvartEn
from engLang.RusBuyEn import RusBuyHomeEn
from engLang.RusBuyEn import RusBuyKommEn
from engLang.GranBuyEn import GranBuyKvartEn
from engLang.GranBuyEn import GranBuyHomeEn
from engLang.GranBuyEn import GranBuyKommEn
from engLang.RusSellEn import RusSellKvartEn
from engLang.RusSellEn import RusSellHomeEn
from engLang.RusSellEn import RusSellKommEn
from engLang.GranSellEn import GranSellKvartEn
from engLang.GranSellEn import GranSellHomeEn
from engLang.GranSellEn import GranSellKommEn
from engLang.BackCallEn import BackCallEn

from engLang import LocationEn

    #============================================================================================================
    #------------------------------------------старт и выбор языка-----------------------------------------------
    #============================================================================================================

@bot.message_handler(commands=['start'])
def start(message):
    global markupLang
    markupLang = types.InlineKeyboardMarkup()

    item_rLang = types.InlineKeyboardButton(text='Русский', callback_data='rusLang')
    item_eLang = types.InlineKeyboardButton(text='English', callback_data='engLang')

    markupLang.add(item_rLang)
    markupLang.add(item_eLang)

    bot.send_message(message.chat.id, 'Выберете язык\nSelect language', reply_markup = markupLang)

    #============================================================================================================
    #----------------------------------------------команды рестарта----------------------------------------------
    #============================================================================================================

@bot.message_handler(content_types=['text'])
def reStart(message):
    if message.text.lower() == 'сначала' or message.text.lower() == 'старт' or message.text.lower() == 'htcnfhn' or message.text.lower() == 'рестарт' or message.text.lower() == 'cnfhn' or message.text.lower() == 'cyfxfkf':
        global markup
        markup = types.InlineKeyboardMarkup()

        item_buy = types.InlineKeyboardButton(text='Хочу купить недвижимость', callback_data='buy')
        item_sell = types.InlineKeyboardButton(text='Хочу продать недвижимость', callback_data='sell')
        item_call = types.InlineKeyboardButton(text='Хочу заказать обратный звонок', callback_data='call')

        markup.add(item_buy)
        markup.add(item_sell)
        markup.add(item_call)

        bot.send_message(message.chat.id, 'Привет!\nНа связи Антон, помогу вам решить вопрос с недвижимостью.\n\nВыберите нужную категорию', reply_markup = markup)
    
    elif message.text.lower() == 'restart' or message.text.lower() == 'reset':
        bot.send_message(message.chat.id, 'Привет!\nНа связи Антон, помогу вам решить вопрос с недвижимостью.\n\nВыберите нужную категорию', reply_markup = markupEn)
    
    #============================================================================================================
    #----------------------------------------главное меню (русский язык)-----------------------------------------
    #============================================================================================================

@bot.callback_query_handler(func = lambda call: True)
def main(call):
    if call.data == 'rusLang':
        global markup
        markup = types.InlineKeyboardMarkup()

        item_buy = types.InlineKeyboardButton(text='Хочу купить недвижимость', callback_data='buy')
        item_sell = types.InlineKeyboardButton(text='Хочу продать недвижимость', callback_data='sell')
        item_call = types.InlineKeyboardButton(text='Хочу заказать обратный звонок', callback_data='call')

        markup.add(item_buy)
        markup.add(item_sell)
        markup.add(item_call)

        bot.send_message(call.message.chat.id, 'Привет!\nНа связи Антон, помогу вам решить вопрос с недвижимостью.\n\nВыберите нужную категорию', reply_markup = markup)

    elif call.data == 'buy':
        global markupBuy
        markupBuy = types.InlineKeyboardMarkup()

        item_rusBuy = types.InlineKeyboardButton(text='В России', callback_data='rusBuy')
        item_granBuy = types.InlineKeyboardButton(text='Другая страна', callback_data='granBuy')
        item_backBuy = types.InlineKeyboardButton(text='Вернуться на шаг назад', callback_data='backBuy')

        markupBuy.add(item_rusBuy)
        markupBuy.add(item_granBuy)
        markupBuy.add(item_backBuy)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Купить недвижимость\n\nВыберите нужную категорию',
        reply_markup=markupBuy)

    elif call.data == 'rest':
         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Привет!\nНа связи Антон, помогу вам решить вопрос с недвижимостью.\n\nВыберите нужную категорию',
        reply_markup = markup)

    elif call.data == 'backBuy':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Привет!\nНа связи Антон, помогу вам решить вопрос с недвижимостью.\n\nВыберите нужную категорию',
        reply_markup = markup)

    #============================================================================================================
    #---------------------------------купить недвижимость в России-----------------------------------------------
    #============================================================================================================

    elif call.data == 'rusBuy':
        global markupRusBuy
        markupRusBuy = types.InlineKeyboardMarkup()

        item_rusBuyKvart = types.InlineKeyboardButton(text='Квартира', callback_data='rusBuyKvart')
        item_rusBuyHome = types.InlineKeyboardButton(text='Дом', callback_data = 'rusBuyHome')
        item_rusBuyKomm = types.InlineKeyboardButton(text='Коммерция', callback_data='rusBuyKomm')
        item_backRusBuy = types.InlineKeyboardButton(text='Вернуться на шаг назад', callback_data='backRusBuy')

        markupRusBuy.add(item_rusBuyKvart, item_rusBuyHome)
        markupRusBuy.add(item_rusBuyKomm)
        markupRusBuy.add(item_backRusBuy)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Купить недвижимость в России\n\nВыберите нужную категорию',
        reply_markup=markupRusBuy)

    #============================================================================================================
    #------------------------------------Выбор типа недвижимости Россия------------------------------------------
    #============================================================================================================

    elif call.data == 'rusBuyKvart':
        bot.send_message(call.message.chat.id, 'Введите название города')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusBuyKvart.sity)

    elif call.data == 'next2':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusBuyKvart.Myname}</b>\n\n<b>Покупка квартиры в России</b>\nГород: <b>{RusBuyKvart.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusBuyKvart.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    elif call.data == 'rusBuyHome':
        bot.send_message(call.message.chat.id, 'Введите название города')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusBuyHome.sity)

    elif call.data == 'next1':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusBuyHome.Myname}</b>\n\n<b>Покупка дома в России</b>\nГород: <b>{RusBuyHome.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusBuyHome.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    elif call.data == 'rusBuyKomm':
        bot.send_message(call.message.chat.id, 'Введите название города')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusBuyKomm.sity)

    elif call.data == 'next3':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusBuyKomm.Myname}</b>\n\n<b>Покупка коммерции в России</b>\nГород: <b>{RusBuyKomm.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusBuyKomm.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    elif call.data == 'backRusBuy':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Купить недвижимость\n\nВыберите нужную категорию', reply_markup=markupBuy)

    #============================================================================================================
    #------------------------------------купить недвижимость за границей-----------------------------------------
    #============================================================================================================

    elif call.data == 'granBuy':
        bot.send_message(call.message.chat.id, 'Введите название страны')
        if call.message.text:
            bot.register_next_step_handler(call.message, Location.country)

    #============================================================================================================
    #----------------------------------Выбор типа недвижимости за границей---------------------------------------
    #============================================================================================================

    elif call.data == 'granBuyKvart':   
        bot.send_message(call.message.chat.id, 'Введите номер телефона')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranBuyKvart.tel)

    elif call.data == 'next8':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranBuyKvart.Myname}</b>\n\n<b>Покупка квартиры за границей</b>\nГород: <b>{Location.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranBuyKvart.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    elif call.data == 'granBuyHome':
        bot.send_message(call.message.chat.id, 'Введите номер телефона')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranBuyHome.tel)

    elif call.data == 'next7':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranBuyHome.Myname}</b>\n\n<b>Покупка дома за границей</b>\nГород: <b>{Location.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranBuyHome.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    elif call.data == 'granBuyKomm':
        bot.send_message(call.message.chat.id, 'Введите номер телефона')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranBuyKomm.tel)

    elif call.data == 'next9':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranBuyKomm.Myname}</b>\n\n<b>Покупка коммерции за границей</b>\nГород: <b>{Location.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranBuyKomm.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    elif call.data == 'backGranBuy':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Купить недвижимость\n\nВыберите нужную категорию', reply_markup=markupBuy)

    #============================================================================================================
    #------------------------------------------продать недвижимость----------------------------------------------
    #============================================================================================================
    
    if call.data == 'sell':
        global markupSell
        markupSell = types.InlineKeyboardMarkup()

        item_rusSell = types.InlineKeyboardButton(text='В России', callback_data='rusSell')
        item_granSell = types.InlineKeyboardButton(text='Другая страна', callback_data='granSell')
        item_backSell = types.InlineKeyboardButton(text='Вернуться на шаг назад', callback_data='backSell')

        markupSell.add(item_rusSell)
        markupSell.add(item_granSell)
        markupSell.add(item_backSell)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Продать недвижимость\n\nВыберите нужную категорию',
        reply_markup=markupSell)

    elif call.data == 'backSell':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Привет!\nНа связи Антон, помогу вам решить вопрос с недвижимостью.\n\nВыберите нужную категорию',
        reply_markup = markup)

    #============================================================================================================
    #---------------------------------продать недвижимость в России----------------------------------------------
    #============================================================================================================

    elif call.data == 'rusSell':
        global markupRusSell
        markupRusSell = types.InlineKeyboardMarkup()

        item_rusSellKvart = types.InlineKeyboardButton(text='Квартира', callback_data='rusSellKvart')
        item_rusSellHome = types.InlineKeyboardButton(text='Дом', callback_data = 'rusSellHome')
        item_rusSellKomm = types.InlineKeyboardButton(text='Коммерция', callback_data='rusSellKomm')
        item_backRusSell = types.InlineKeyboardButton(text='Вернуться на шаг назад', callback_data='backRusSell')

        markupRusSell.add(item_rusSellKvart, item_rusSellHome)
        markupRusSell.add(item_rusSellKomm)
        markupRusSell.add(item_backRusSell)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Продать недвижимость в России\n\nВыберите нужную категорию',
        reply_markup=markupRusSell)

    #============================================================================================================
    #---------------------------------Выбор типа недвижимости Россия (продажа)-----------------------------------
    #============================================================================================================

    elif call.data == 'rusSellKvart':
        bot.send_message(call.message.chat.id, 'Введите название города')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusSellKvart.sity)

    elif call.data == 'next5':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusSellKvart.Myname}</b>\n\n<b>Продажа квартиры в России</b>\nГород: <b>{RusSellKvart.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusSellKvart.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    elif call.data == 'rusSellHome':
        bot.send_message(call.message.chat.id, 'Введите название города')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusSellHome.sity)

    elif call.data == 'next4':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusSellHome.Myname}</b>\n\n<b>Продажа дома в России</b>\nГород: <b>{RusSellHome.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusSellHome.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    elif call.data == 'rusSellKomm':
        bot.send_message(call.message.chat.id, 'Введите название города')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusSellKomm.sity)

    elif call.data == 'next6':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusSellKomm.Myname}</b>\n\n<b>Продажа коммерции в России</b>\nГород: <b>{RusSellKomm.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusSellKomm.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    elif call.data == 'backRusSell':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Продать недвижимость\n\nВыберите нужную категорию', reply_markup=markupSell)

    #============================================================================================================
    #-----------------------------------продать недвижимость за границей-----------------------------------------
    #============================================================================================================

    elif call.data == 'granSell':
        bot.send_message(call.message.chat.id, 'Введите название страны')
        if call.message.text:
            bot.register_next_step_handler(call.message, Location.countrySell)

    #============================================================================================================
    #--------------------------------Выбор типа недвижимости за границей (продажа)-------------------------------
    #============================================================================================================

    elif call.data == 'granSellKvart':   
        bot.send_message(call.message.chat.id, 'Введите номер телефона')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranSellKvart.tel)

    elif call.data == 'next11':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranSellKvart.Myname}</b>\n\n<b>Продажа квартиры за границей</b>\nГород: <b>{Location.SitySell}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranSellKvart.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup) 

    elif call.data == 'granSellHome':
        bot.send_message(call.message.chat.id, 'Введите номер телефона')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranSellHome.tel)

    elif call.data == 'next10':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranSellHome.Myname}</b>\n\n<b>Продажа дома за границей</b>\nГород: <b>{Location.SitySell}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranSellHome.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)            

    elif call.data == 'granSellKomm':
        bot.send_message(call.message.chat.id, 'Введите номер телефона')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranSellKomm.tel)

    elif call.data == 'next12':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranSellKomm.Myname}</b>\n\n<b>Продажа коммерции за границей</b>\nГород: <b>{Location.SitySell}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranSellKomm.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup) 

    elif call.data == 'backGranSell':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Продать недвижимость\n\nВыберите нужную категорию', reply_markup=markupSell)

    #============================================================================================================
    #----------------------------------------------Обратный звонок-----------------------------------------------
    #============================================================================================================   

    elif call.data == 'call':
        bot.send_message(call.message.chat.id, 'Введите номер телефона')
        if call.message.text:
            bot.register_next_step_handler(call.message, BackCall.tel)

    elif call.data == 'next':
        restMarkup = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='Сначала', callback_data='rest')
        restMarkup.add(item_res)

        bot.send_message('@bottgdb', f'<b>{BackCall.Myname}</b>\n\n<b>Обратный звонок</b>\n\nСвязь со мной:\nНомер телефона: <b>{BackCall.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Спасибо за обращение!\nМы скоро свяжемся с вами', reply_markup=restMarkup)

    #============================================================================================================
    #-----------------------------------главное меню (Английский язык)------------------------------------------- 
    #============================================================================================================

    elif call.data == 'engLang':
        global markupEn
        markupEn = types.InlineKeyboardMarkup()

        item_buyEn = types.InlineKeyboardButton(text='Buy realty', callback_data='buyEn')
        item_sellEn = types.InlineKeyboardButton(text='Sell realty', callback_data='sellEn')
        item_callEn = types.InlineKeyboardButton(text='Order a callback', callback_data='callEn')

        markupEn.add(item_buyEn)
        markupEn.add(item_sellEn)
        markupEn.add(item_callEn)

        bot.send_message(call.message.chat.id, 'Hi!\nAnton is in touch, I will help you solve the real estate issue.\n\nSelect the desired category', reply_markup = markupEn)

    #============================================================================================================
    #---------------------------------купить недвижимость в России-----------------------------------------------
    #============================================================================================================

    elif call.data == 'buyEn':
        global markupBuyEn
        markupBuyEn = types.InlineKeyboardMarkup()

        item_rusBuyEn = types.InlineKeyboardButton(text='In Russia', callback_data='rusBuyEn')
        item_granBuyEn = types.InlineKeyboardButton(text='Another country', callback_data='granBuyEn')
        item_backBuyEn = types.InlineKeyboardButton(text='Go back a step', callback_data='backBuyEn')

        markupBuyEn.add(item_rusBuyEn)
        markupBuyEn.add(item_granBuyEn)
        markupBuyEn.add(item_backBuyEn)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Buy real estate\n\nSelect the desired category',
        reply_markup=markupBuyEn)

    elif call.data == 'restEn':
         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Hi!\nAnton is in touch, I will help you solve the real estate issue.\n\nSelect the desired category',
        reply_markup = markupEn)

    elif call.data == 'backBuyEn':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Hi!\nAnton is in touch, I will help you solve the real estate issue.\n\nSelect the desired category',
        reply_markup = markupEn)

    #============================================================================================================
    #---------------------------------купить недвижимость в России-----------------------------------------------
    #============================================================================================================

    elif call.data == 'rusBuyEn':
        global markupRusBuyEn
        markupRusBuyEn = types.InlineKeyboardMarkup()

        item_rusBuyKvartEn = types.InlineKeyboardButton(text='Apartment', callback_data='rusBuyKvartEn')
        item_rusBuyHomeEn = types.InlineKeyboardButton(text='House', callback_data = 'rusBuyHomeEn')
        item_rusBuyKommEn = types.InlineKeyboardButton(text='Commerce', callback_data='rusBuyKommEn')
        item_backRusBuyEn = types.InlineKeyboardButton(text='Go back a step', callback_data='backRusBuyEn')

        markupRusBuyEn.add(item_rusBuyKvartEn, item_rusBuyHomeEn)
        markupRusBuyEn.add(item_rusBuyKommEn)
        markupRusBuyEn.add(item_backRusBuyEn)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Buy real estate in Russia\n\nSelect the desired category',
        reply_markup=markupRusBuyEn)

    #============================================================================================================
    #------------------------------------Выбор типа недвижимости Россия------------------------------------------
    #============================================================================================================

    elif call.data == 'rusBuyKvartEn':
        bot.send_message(call.message.chat.id, 'Enter the name of the city')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusBuyKvartEn.sity)

    elif call.data == 'nextEn2':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusBuyKvartEn.Myname}</b>\n\n<b>Покупка квартиры в России</b>\nГород: <b>{RusBuyKvartEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusBuyKvartEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

    elif call.data == 'rusBuyHomeEn':
        bot.send_message(call.message.chat.id, 'Enter the name of the city')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusBuyHomeEn.sity)

    elif call.data == 'nextEn1':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusBuyHomeEn.Myname}</b>\n\n<b>Покупка дома в России</b>\nГород: <b>{RusBuyHomeEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusBuyHomeEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

    elif call.data == 'rusBuyKommEn':
        bot.send_message(call.message.chat.id, 'Enter the name of the city')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusBuyKommEn.sity)

    elif call.data == 'nextEn3':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusBuyKommEn.Myname}</b>\n\n<b>Покупка коммерции в России</b>\nГород: <b>{RusBuyKommEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusBuyKommEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

    elif call.data == 'backRusBuyEn':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Sell real estate\n\nSelect the desired category', reply_markup=markupBuyEn)

    #============================================================================================================
    #------------------------------------купить недвижимость за границей-----------------------------------------
    #============================================================================================================

    elif call.data == 'granBuyEn':
        bot.send_message(call.message.chat.id, 'Enter the name of the country')
        if call.message.text:
            bot.register_next_step_handler(call.message, LocationEn.country)

    #============================================================================================================
    #----------------------------------Выбор типа недвижимости за границей---------------------------------------
    #============================================================================================================

    elif call.data == 'granBuyKvartEn':   
        bot.send_message(call.message.chat.id, 'Enter your phone number')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranBuyKvartEn.tel)

    elif call.data == 'nextEn8':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranBuyKvartEn.Myname}</b>\n\n<b>Покупка квартиры за границей</b>\nГород: <b>{LocationEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranBuyKvartEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

    elif call.data == 'granBuyHomeEn':
        bot.send_message(call.message.chat.id, 'Enter your phone number')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranBuyHomeEn.tel)

    elif call.data == 'nextEn7':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranBuyHomeEn.Myname}</b>\n\n<b>Покупка дома за границей</b>\nГород: <b>{LocationEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranBuyHomeEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

    elif call.data == 'granBuyKommEn':
        bot.send_message(call.message.chat.id, 'Enter your phone number')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranBuyKommEn.tel)

    elif call.data == 'nextEn9':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranBuyKommEn.Myname}</b>\n\n<b>Покупка коммерции за границей</b>\nГород: <b>{LocationEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranBuyKommEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

    elif call.data == 'backGranBuyEn':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Buy real estate\n\nSelect the desired category', reply_markup=markupBuyEn)

    #============================================================================================================
    #----------------------------------------продать недвижимость------------------------------------------------
    #============================================================================================================
    
    if call.data == 'sellEn':
        global markupSellEn
        markupSellEn = types.InlineKeyboardMarkup()

        item_rusSellEn = types.InlineKeyboardButton(text='In Russia', callback_data='rusSellEn')
        item_granSellEn = types.InlineKeyboardButton(text='Another country', callback_data='granSellEn')
        item_backSellEn = types.InlineKeyboardButton(text='Go back a step', callback_data='backSellEn')

        markupSellEn.add(item_rusSellEn)
        markupSellEn.add(item_granSellEn)
        markupSellEn.add(item_backSellEn)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Sell real estate\n\nSelect the desired category',
        reply_markup=markupSellEn)

    elif call.data == 'backSellEn':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Hi!\nAnton is in touch, I will help you solve the real estate issue.\n\nSelect the desired category',
        reply_markup = markupEn)

    #============================================================================================================
    #---------------------------------продать недвижимость в России----------------------------------------------
    #============================================================================================================

    elif call.data == 'rusSellEn':
        global markupRusSellEn
        markupRusSellEn = types.InlineKeyboardMarkup()

        item_rusSellKvartEn = types.InlineKeyboardButton(text='Apartment', callback_data='rusSellKvartEn')
        item_rusSellHomeEn = types.InlineKeyboardButton(text='House', callback_data = 'rusSellHomeEn')
        item_rusSellKommEn = types.InlineKeyboardButton(text='Commerce', callback_data='rusSellKommEn')
        item_backRusSellEn = types.InlineKeyboardButton(text='Go back a step', callback_data='backRusSellEn')

        markupRusSellEn.add(item_rusSellKvartEn, item_rusSellHomeEn)
        markupRusSellEn.add(item_rusSellKommEn)
        markupRusSellEn.add(item_backRusSellEn)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Sell real estate in Russia\n\nSelect the desired category',
        reply_markup=markupRusSellEn)

    #============================================================================================================
    #---------------------------------Выбор типа недвижимости Россия (продажа)-----------------------------------
    #============================================================================================================

    elif call.data == 'rusSellKvartEn':
        bot.send_message(call.message.chat.id, 'Enter the name of the city')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusSellKvartEn.sity)

    elif call.data == 'nextEn5':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusSellKvartEn.Myname}</b>\n\n<b>Продажа квартиры в России</b>\nГород: <b>{RusSellKvartEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusSellKvartEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

    elif call.data == 'rusSellHomeEn':
        bot.send_message(call.message.chat.id, 'Enter the name of the city')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusSellHomeEn.sity)

    elif call.data == 'nextEn4':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusSellHomeEn.Myname}</b>\n\n<b>Продажа дома в России</b>\nГород: <b>{RusSellHomeEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusSellHomeEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

    elif call.data == 'rusSellKommEn':
        bot.send_message(call.message.chat.id, 'Enter the name of the city')
        if call.message.text:
            bot.register_next_step_handler(call.message, RusSellKommEn.sity)

    elif call.data == 'nextEn6':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{RusSellKommEn.Myname}</b>\n\n<b>Продажа коммерции в России</b>\nГород: <b>{RusSellKommEn.Sity}</b>\n\nСвязь со мной:\nНомер телефона: <b>{RusSellKommEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

    elif call.data == 'backRusSellEn':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Sell real estate\n\nSelect the desired category', reply_markup=markupSellEn)

    #============================================================================================================
    #-----------------------------------продать недвижимость за границей-----------------------------------------
    #============================================================================================================

    elif call.data == 'granSellEn':
        bot.send_message(call.message.chat.id, 'Enter the name of the country')
        if call.message.text:
            bot.register_next_step_handler(call.message, LocationEn.countrySell)

    #============================================================================================================
    #--------------------------------Выбор типа недвижимости за границей (продажа)-------------------------------
    #============================================================================================================

    elif call.data == 'granSellKvartEn':   
        bot.send_message(call.message.chat.id, 'Enter your phone number')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranSellKvartEn.tel)

    elif call.data == 'nextEn11':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranSellKvartEn.Myname}</b>\n\n<b>Продажа квартиры за границей</b>\nГород: <b>{LocationEn.SitySell}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranSellKvartEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn) 

    elif call.data == 'granSellHomeEn':
        bot.send_message(call.message.chat.id, 'Enter your phone number')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranSellHomeEn.tel)

    elif call.data == 'nextEn10':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranSellHomeEn.Myname}</b>\n\n<b>Продажа дома за границей</b>\nГород: <b>{LocationEn.SitySell}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranSellHomeEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)    

    elif call.data == 'granSellKommEn':
        bot.send_message(call.message.chat.id, 'Enter your phone number')
        if call.message.text:
            bot.register_next_step_handler(call.message, GranSellKommEn.tel)

    elif call.data == 'nextEn12':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{GranSellKommEn.Myname}</b>\n\n<b>Продажа коммерции за границей</b>\nГород: <b>{LocationEn.SitySell}</b>\n\nСвязь со мной:\nНомер телефона: <b>{GranSellKommEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn) 

    elif call.data == 'backGranSellEn':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='-Sell real estate\n\nSelect the desired category', reply_markup=markupSellEn)

    #============================================================================================================
    #----------------------------------------------Обратный звонок-----------------------------------------------
    #============================================================================================================   

    elif call.data == 'callEn':
        bot.send_message(call.message.chat.id, 'Enter your phone number')
        if call.message.text:
            bot.register_next_step_handler(call.message, BackCallEn.tel)

    elif call.data == 'nextEn':
        restMarkupEn = types.InlineKeyboardMarkup()
        item_res = types.InlineKeyboardButton(text='At the begining', callback_data='restEn')
        restMarkupEn.add(item_res)

        bot.send_message('@bottgdb', f'<b>{BackCallEn.Myname}</b>\n\n<b>Обратный звонок</b>\n\nСвязь со мной:\nНомер телефона: <b>{BackCallEn.phoneNum}</b>\neMail: <b>Нет</b>', parse_mode='html')
        bot.send_message(call.message.chat.id, 'Thank you for contacting us!\nWe will contact you soon', reply_markup=restMarkupEn)

bot.polling(non_stop=True)