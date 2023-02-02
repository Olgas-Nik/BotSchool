Если вам необходимо узнать гороскоп на сегодня, и проверить какое число сегодня ваше, тогда вам следует подключиться к моему боту!!! https://t.me/Pilka25_bot
Ниже небольшая шпаргалка, как он создавлася.
Регистрируем бота в Телеграме через запрос @BotFather. 
Нажимаем Start и пишем команду /newbot. Придумываем название бота и его ниекнейм.
Устанавливаем Python-библиотеку для работы с Телеграмом: pip isnatll pytelegrambotapi
Подключаем библиотеку import telebot, bot = telebot.Telebot('token')
Пишем код с командами и добавляем кнопки.
В данном боте я использовала два вида кнопок: Inline(url) и обычные Reply
Inline - кнопки вы видите под сообщением. Используется тип  markup = types.InlineKeyboardMarkup(),  btn1 = types.InlineKeyboardButton(text='', callback_data='btn1'), markup.add(btn1)
Reply - кнопки вы видите вместо клавиатуры. Используется тип markup = types.ReplyKeyboardMarkup(resize_keyboard=True), btn1 = types.KeyboardButton(" "), markup.add(btn1)
Это мой первый бот, поэтому не судите строго;)
