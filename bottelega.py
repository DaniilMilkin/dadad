import telebot

bot = telebot.TeleBot('1406471510:AAGF0uSxIqhlq-ALEgfvA_A5Be5jgSkKoQs')

@bot.message_handler(content_types=['text'])

def send_text(message):

     if message.text == 'Привет!':

         bot.send_message(message.chat.id, 'Привет!')



     elif message.text == 'Как тебя зовут?':
        bot.send_message(message.chat.id, 'Bot1')
    
     elif message.text == 'Как дела?':
        bot.send_message(message.chat.id, 'Нормально,а твои?')

     elif message.text == 'Что ты умеешь делать?':
        bot.send_message(message.chat.id, 'Отвечать на твои сообщения')

     elif message.text == 'Сколько градусов на улеце?':
        bot.send_message(message.chat.id, '-3')  

     elif message.text == 'Извени,я занят напишу завтра ':
        bot.send_message(message.chat.id, 'Ок') 

     elif message.text == 'Ссылка на картинки с животными':
        bot.send_message(message.chat.id, 'https://www.google.com/search?q=%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8+%D1%81+%D0%B6%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%BC%D0%B8&tbm=isch&ved=2ahUKEwjTtJKU27HtAhUS6CoKHSk9Cs8Q2-cCegQIABAA&oq=%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8+%D1%81+%D0%B6%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%BC%D0%B8&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgAEEM6BggAEAUQHjoGCAAQCBAeOgQIABAYOgUIABCxAzoICAAQsQMQgwE6BwgAELEDEENQ_rMIWPyWCWCFoQloAHAAeASAAZ4BiAGDIJIBBDEuMzOYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAMABAQ&sclient=img&ei=gczIX5PwJJLQqwGp-qj4DA&bih=969&biw=1920')

     elif message.text == 'Какое твое любимое животное?':
        bot.send_message(message.chat.id, 'Собака') 

     elif message.text == 'Любимая еда?':
        bot.send_message(message.chat.id, 'Вода')

     elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Пока')                  

     else:
        atext = message.text[:3] + message.text.lower()
        bot.send_message(message.chat.id, atext)

bot.polling()