import config
import telebot
from config import token
from telebot import types

# URL = "https://1001goroskop.ru/?tm=love"
# r = requests.get(URL)
# print(r.status_code)
# print(r.text)
# soup = bs(r.text, 'html.parser')
# horoscope = soup.find_all('div', itemprop_="description")
# print(horoscope)


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓Что бот предлагает?")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, ".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "👋 Поздороваться":
        bot.send_message(message.chat.id, text="У меня для тебя кое что интересное?")
    elif message.text == "❓Что бот предлагает?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Нумерология')
        item2 = types.KeyboardButton('Гороскоп')
        # back = types.KeyboardButton('Вернуться в главное меню')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Выбери Нумерология или Гороскоп? ".format(name=message.text), reply_markup=markup)

    elif message.text == "Нумерология":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='1', callback_data='btn1')
        btn2 = types.InlineKeyboardButton(text='2', callback_data='btn2')
        btn3 = types.InlineKeyboardButton(text='3', callback_data='btn3')
        markup.add(btn1, btn2, btn3)
        btn4 = types.InlineKeyboardButton(text='4', callback_data='btn4')
        btn5 = types.InlineKeyboardButton(text='5', callback_data='btn5')
        btn6 = types.InlineKeyboardButton(text='6', callback_data='btn6')
        markup.add(btn4, btn5, btn6)
        btn7 = types.InlineKeyboardButton(text='7', callback_data='btn7')
        btn8 = types.InlineKeyboardButton(text='8', callback_data='btn8')
        btn9 = types.InlineKeyboardButton(text='9', callback_data='btn9')
        markup.add(btn7, btn8, btn9)
        bot.send_message(message.chat.id, 'Выбери номер от 1 до 9', reply_markup=markup)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif message.text == "Гороскоп":
        markup = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton('♈️Овен♈️', callback_data='key_oven')
        key_telec = types.InlineKeyboardButton('♉️Телец♉️', callback_data='key_telec')
        markup.add(key_oven, key_telec)
        key_bliznecy = types.InlineKeyboardButton('♊️Близнецы♊️', callback_data='key_bliznecy')
        key_rak = types.InlineKeyboardButton('♋️Рак♋️', callback_data='key_rak')
        markup.add(key_bliznecy, key_rak)
        key_lev = types.InlineKeyboardButton('️♌️Лев♌️', callback_data='key_lev')
        key_deva = types.InlineKeyboardButton('♍️Дева♍️', callback_data='key_deva')
        markup.add(key_lev, key_deva)
        key_vesy = types.InlineKeyboardButton('♎️Весы♎️', callback_data='key_vesy')
        key_scorpion = types.InlineKeyboardButton('♏️Скорпион♏️', callback_data='key_scorpion')
        markup.add(key_vesy, key_scorpion)
        key_strelec = types.InlineKeyboardButton('♐️Стрелец♐️', callback_data='key_strelec')
        key_kozerog = types.InlineKeyboardButton('♑️Козерог♑️', callback_data='key_kozerog')
        markup.add(key_strelec, key_kozerog)
        key_vodoley = types.InlineKeyboardButton('♒️Водолей♒️', callback_data='key_vodoley')
        key_ryby = types.InlineKeyboardButton('♓️Рыбы♓️', callback_data='key_ryby')
        markup.add(key_vodoley, key_ryby)
        bot.send_message(message.chat.id, "Выбери свой знак зодиака", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == "key_oven":
        bot.send_message(callback.message.chat.id, "Овен, Приоткройте завесу, которая отделяет ваш внутренний мир от окружающих. Это поможет вам понять, и быть понятым самому." )
    elif callback.data == "key_telec":
        bot.send_message(callback.message.chat.id, "Телец, Не ешьте сегодня на завтрак тяжелой пищи, это поможет вам сохранить хорошее настроение до конца дня. На работе постарайтесь остаться в стороне от излишне горячих дискуссий.")
    elif callback.data == "key_bliznecy":
        bot.send_message(callback.message.chat.id, "Близнец, Намерения ваши прекрасны, но время для их осуществления сегодня если не худшее, то достаточно неудачное, чтобы отложить эту затею. Только не забывайте о ней совсем. Жалко, если пропадет такое начинание.")
    elif callback.data == "key_rak":
        bot.send_message(callback.message.chat.id, "Рак. Сегодня вам удастся достичь золотой середины в вопросе определения количества информации, необходимого для максимально продуктивной работы вашего мозга. Придерживайтесь ее, сколько сможете.")
    elif callback.data == "key_lev":
        bot.send_message(callback.message.chat.id, "Лев, Сегодня у вас появится реальная возможность уговорить тех, кто ранее уговорам не поддавался. Но сила убеждения - оружие обоюдоострое. При неаккуратном обращении можно уговорить на любое сколь угодно глупое действие самого себя.")
    elif callback.data == "key_deva":
        bot.send_message(callback.message.chat.id, "Дева, Сегодня настанет, наконец, момент, когда откладывать дальше принятие решения станет невозможно, ибо в противном случае решение рискует остаться непринятым, а вы будете загрызены собственной совестью.")
    elif callback.data == "key_vesy":
        bot.send_message(callback.message.chat.id, "Весы, Сегодня вы можете стать жертвой апатии, возможно надолго. Лучший способ борьбы с ней - профилактика. Не давайте себе отдыха, и, возможно, она не сможет к вам подобраться.")
    elif callback.data == "key_scorpion":
        bot.send_message(callback.message.chat.id, "Скорпион, Сегодня постарайтесь не обнародовать свое истинное мнение по данному вопросу. От вас ждут сочувствия, и ничего иного.")
    elif callback.data == "key_strelec":
        bot.send_message(callback.message.chat.id, "Стрелец, Сегодня вы можете стать жертвой апатии, возможно надолго. Лучший способ борьбы с ней - профилактика. Не давайте себе отдыха, и, возможно, она не сможет к вам подобраться.")
    elif callback.data == "key_kozerog":
        bot.send_message(callback.message.chat.id, "Козерог, Не старайтесь найти причину для печали - не найдете. И учтите, что ваше хорошее настроение на редкость заразительно. Так что к недругам даже подходить не стоит, дабы не заразить.")
    elif callback.data == "key_vodoley":
        bot.send_message(callback.message.chat.id, "Водолей, Полагайтесь сегодня только на здравый смысл. Если вы чувствуете, что вам его недостает, стоит воспользоваться чужим. Делайте что угодно, но не давайте воли эмоциям.")
    elif callback.data == "key_ryby":
        bot.send_message(callback.message.chat.id, "Рыбы, Вас ждет весьма захватывающий вечер. Подготовьтесь к нему.")
    elif callback.data == "btn1":
        bot.send_message(callback.message.chat.id, "Приятным станет поход на рынок или в какой-нибудь супермаркет. Покупки, сделанные сегодня, порадуют, а приобретённые вами вещи будут служить достаточно долго.")
    elif callback.data == "btn2":
        bot.send_message(callback.message.chat.id, "Если вы хотите, чтобы день прошел позитивно, постарайтесь с самого утра держать себя в руках и не поддаваться эмоциям. ")
    elif callback.data == "btn3":
        bot.send_message(callback.message.chat.id, "Дела обещают идти без лишней суеты, а принятые решения будут отличаться взвешенностью.")
    elif callback.data == "btn4":
        bot.send_message(callback.message.chat.id, "День не склоняет к флирту и мимолетным романам, зато идеален для того, чтобы провести его с любимым человеком")
    elif callback.data == "btn5":
        bot.send_message(callback.message.chat.id, "Чтобы идти вперед, необходимо избавиться от старых комплексов и клише. ")
    elif callback.data == "btn6":
        bot.send_message(callback.message.chat.id, "Пора перестать относиться к жизни слишком серьезно, а к своему любимому человеку – слишком требовательно")
    elif callback.data == "btn7":
        bot.send_message(callback.message.chat.id, "Возможность провести время рядом с человеком, который появился на его горизонте не случайно и, вполне возможно, сыграет в его дальнейшей судьбе важную роль. ")
    elif callback.data == "btn8":
        bot.send_message(callback.message.chat.id, "Стихийная внезапность способна привнести в дела свежую струю и множество оригинальных идей, а осторожная, вдумчивая твердость оградит от непродуманных действий.")
    elif callback.data == "btn9":
        bot.send_message(callback.message.chat.id, "Осторожнее: чувства в этот день вполне могут вскружить вам голову.")




bot.polling(none_stop=True, interval=0)

