import time
import os
import telebot
import pandas
import feedparser
import random
import schedule
import requests
import json
from easygoogletranslate import EasyGoogleTranslate
from datetime import datetime
from time import mktime
from multiprocessing import *
from telebot import types


TOKEN = "5218759908:AAFRlXyzPtk-25nmMjOCexKpSO4W9L_DkRQ"
bot = telebot.TeleBot(TOKEN)
group_id = "-1001579039420"
translator = EasyGoogleTranslate(
    source_language='en',
    target_language='ru',
    timeout=10
)

def start_process():
    p1 = Process(target=TimeSchedule.start_schedule, args=()).start()

class TimeSchedule():
    def start_schedule():
        schedule.every().day.at("00:00").do(TimeSchedule.send_congratulations)
        schedule.every().day.at("21:08").do(TimeSchedule.nicejoke)

        while True:
            schedule.run_pending()
            time.sleep(1)


    def send_congratulations():
        data = pandas.read_csv("birthdays.csv")
        today = datetime.now()
        today_tuple = (today.month, today.day)
        birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

        if today_tuple in birthdays_dict:
            birthday_person = birthdays_dict[today_tuple]
            name = birthday_person["name"]
            bot.send_message(group_id, f"С Днём Рождения {name}! 🥳🥳🥳👋👋👋🔈🔈🔈🍺🍺🍺🍻🍻🍻😃😃😃")
        else:
            bot.send_message(group_id, 'Сегодня нет именинников.')
    def nicejoke():
        req = requests.get("https://api.humorapi.com/jokes/random?api-key=ddb5a27446fc44f4b87496e160b46711").text
        jsonText = json.loads(req)
        lolkek = jsonText["joke"]
        result = translator.translate(lolkek)
        bot.send_message(group_id, result)

@bot.message_handler(regexp='Оптя как ты?')
def event(message):
    random_answer_event = ['По каналу Кино ТВ Криминальное чтиво идёт 😎👌',
                        'Ребята у меня с 18 декабря отпуск . Я всё таки Вас соберу !',
                        'По тв 3 Шакал начался с Брюсом Уильямсом',
                        'Я всегда за👍🙏🥳',
                        'Ребзя, я в кино...',
                        'Хочу Хардкор!!!🤦‍♂️🤦‍♂️🤦‍♂️🥳🥳🥳🙃🙃🙃',
                        'Я в Старом амбаре в седьмом...))) Паспорт загранник получил!)))',
                        'Да я уж дома...))) Хотел пивас попить после работы...)))',
                        'Сейчас приеду 🤣🤣🤣',
                        'Куда ехать?🤣🤣🤣🤦‍♂️🤦‍♂️🤦‍♂️👻👻👻',
                        'Фашиста слушаю Казантип 2004 год 🔥🔥👌😊👏👏👏💯💯💯',
                        'На фильм Скандал пошёл.)))) Уж больно мне актрисы нравятся 😜😃😃😃',
                        'У кого какие соображения?',
                        'Когда сход ребзя?!',
                        'Начались тупые вопросы 🤦‍♂️🤦‍♂️🤦‍♂️🤣🤣🤣🤩🤩🤩',
                        'Я тут одно мужичка нашёл, наверное мой одногодка, музыку пишет электронную Ильшат Газизов. Как нибудь его пригласим к нам на сход!))))',
                        'Ребята я в отпуск 🥳🥳🥳🍻🍻🍻👏👏👏👏👏👏👏👌😃',
                        'Ребята пока я в отпуске, может как нибудь в тихоря стрелбан? У кого есть какие соображения?',
                        'Я+']
    
    bot.send_message(message.chat.id, random.choice(random_answer_event))

@bot.message_handler(regexp='Оптя ты лох')
def start(message):
    random_audio = open('audio/' + random.choice(os.listdir('audio')), 'rb')
    bot.send_audio(message.chat.id, random_audio) 
    random_audio.close()

@bot.message_handler(content_types=["pinned_message", "photo", "voice", "video"])
def reply_genius(message):
    random_answer = [
                    'Гениально 👍👍👍🔥🔥🔥🥰🥰🥰😃😃😃',
                    'Спасибо судья 👍🔥😊😊😊', 
                    'Гениально 👍👍👍👍👏👏👏😁😁😁',
                    'Спаси сохрани 🙏🙏🙏🤦‍♂️🤦‍♂️🤦‍♂️🤣🤣🤣',
                    'Я в шоке!!!🤦‍♂️🤦‍♂️🤦‍♂️🙏🙏🙏😃😃😃🔥🔥🔥🥰🥰🥰',
                    'Если честно мне этот телеграмм не нравится. Ватсапу больше предпочтение...(((((',
                    'Вот что бывает когда не пьёшь и за здоровый образ, кукушка ехать начинает.))))))',
                    '👍👍👍👍',
                    'От души 🔥🔥🔥🥰🥰🥰👍👍👍',
                    'Гуд 😁😁😁👍👍👍',
                    'От души, дружище, Спасибо!!!🔥🔥🔥💯💯💯😍😍💪💪💪🙏🙏👍🥩🥩🥩',
                    'Спасибо!!!!👍👍👍🔥🔥🔥💯💯💯🥰🥰🥰',
                    'Спасибо большое Вам!!🔥🔥🔥💯😍😍😍👍👍👍',
                    'Спасибо большое 👍👍👍🔥🔥🔥💯💯🥰🥰🥰',
                    '👍👍👍🔥🔥🔥💯💯💯🥩🥩🥩🥰🥰🥰👍👍👍👍',
                    '🔈🔈🔈🥰🥰🥰🥩🥩🥩🔥🔥🔥💯💯💯👍👍👍😘😘😘'
                    'Это очередной шедевр 🔥🔥🔥🔥👍👍👍👏👏👏',
                    ]
    bot.send_message(message.chat.id, random.choice(random_answer), reply_to_message_id=message.message_id)

@bot.message_handler(regexp='Оптя как дела?')
def reply_kakdela(message):
    random_answer = [
                    'мое уважение к тебе не настолько велико чтобы считаться друзьями и рассказывать правду про мои дела',
                    'я дед инсайд',
                    'у роботов дела всегда стабильно',
                    'зачем тебе эта информация?\nя тебе не отвечу, недостаточно доверия к тебе.',
                    ]
    bot.send_message(message.chat.id, random.choice(random_answer), reply_to_message_id=message.message_id)

@bot.message_handler(regexp='Оптя ты гей?')
def reply_areugay(message):
    random_answer = [
                    'Да.',
                    'Только для тебя',
                    'У машин нет чувств',
                    'Я люблю роботов',
                    'Да, нахуй этих вумен...',
                    ]
    bot.send_message(message.chat.id, random.choice(random_answer), reply_to_message_id=message.message_id)

@bot.message_handler(regexp='Оптя как думаешь, нужно ли мне')
def reply_areugay(message):
    random_answer = [
                    'Бесспорно.',
                    'Предрешено..',
                    'Никаких сомнений',
                    'Определённо да',
                    'Можешь быть уверен в этом',
                    'Мне кажется — «да»',
                    'Вероятнее всего',
                    'Хорошие перспективы',
                    'Знаки говорят — «да»',
                    'Да',
                    'Пока не ясно, попробуй снова',
                    'Спроси через 5 минут',
                    'Лучше тебе не знать...',
                    'Сейчас нельзя предсказать',
                    'Сконцентрируйся и спроси опять',
                    'Даже не думай',
                    'Мой ответ — «нет»',
                    'По моим данным — «нет»',
                    'Перспективы не очень хорошие',
                    'Весьма сомнительно',                    
                    ]
    bot.send_message(message.chat.id, random.choice(random_answer), reply_to_message_id=message.message_id)

'''@bot.message_handler(regexp='ахах')
def greet(message):
    text = requests.get("https://insult.mattbas.org/api/insult").text
    result = translator.translate(text)
    bot.reply_to(message, result)
'''
@bot.message_handler(regexp='Оптя я тебя люблю')
def iloveyou(message):
    random_answer = ['Я тоже тебя люблю',
                     'Я смущен',
                     '👉👈🥺',
                    ]
    bot.send_message(message.chat.id, random.choice(random_answer), reply_to_message_id=message.message_id)



@bot.message_handler(regexp='Оптя расскажи шутку')
def superjoke(message):
    name = message.from_user.first_name
    random_answer = [
                    f'— Подсудимый {name}, встаньте. Вы обвиняетесь в групповом изнасиловании. Вам все понятно?\n— Да\n— Садитесь.\nГруппа изнасилованных, встаньте.',       
                    f'— Мам, пап, смотрите! Это мой новый друг Алёша.\n— Бля, да это же мёртвый лось!\n— Пойдём, {name}. Нам тут не рады.',
                    f'Засунул {name} жопу 10 копеек.\nМелочь, а приятно,',
                    f'В дом к {name} забрались воры. Попали в подвал. А там бочонки с вином. Выпили. — Давай еще немного выпьем, и тихо—тихо попоем. Попели. — Давай еще немного выпьем, и тихо—тихо потанцуем. Потанцевали. — Давай еще немного выпьем и тихо—тихо постреляем. Постреляли. Входит хозяин: — Вах! Вах! Вах! В доме гости, а я сплю!',
                    f'В дверь не стучали\n— Ник Вуйчич! - догадался {name}.',
                    f'Идет {name} по улице. Тащит два арбуза подмышками. Тут его мужик спрашивает:\n— Сколько времени?\n{name}:\n— Слющай, падержи арбузи...\nМужик взял. {name} (разводя руками):\n— Откюда я знаю?',
                    '— Ёбаный рот этого приемного пункта, блядь! Ты кто такой?\n— Нудист.\n— Почему одетый?\n— Извращенец.',
                    'Очень грустная китайская история :\n朣楢琴执㝧执瑩浻牡楧㩮㔱硰执㝧执獧浻牡楧敬瑦瀰絸朣杢㑳执獧扻捡杫潲湵潣潬㩲昣昸昸 㬸慢正牧畯摮椭慭敧敷止瑩札慲楤湥楬敮牡氬晥⁴潴敬瑦戠瑯潴牦浯㡦㡦㡦潴捥捥捥戻捡杫潲湵浩条㩥眭扥楫楬敮牡札慲楤湥潴昣昸昸攣散散戻捡杫潲湵浩条㩥洭穯氭湩慥牧摡敩瑮琨灯㡦㡦㡦捥捥捥㬩慢正牧畯摮椭慭敧獭氭湩慥牧摡敩瑮琨灯㡦㡦㡦捥捥捥㬩慢正牧畯摮椭慭敧楬敮牡札慲楤湥潴昣昸昸攣散散戻捡杫潲湵浩条㩥楬敮牡札慲楤湥潴昣昸昸攣散散汩整\nАртас! Сын мой! Что ты делаешь?!',
                    'Одному парню понравилась девушка.\nОн подошел к ней',
                    'Что делают негры в Африке, чтобы не умереть от СПИДа?\nУмирают от голода',
                    'бля я заебался...',
                    ]
    bot.send_message(message.chat.id, random.choice(random_answer), reply_to_message_id=message.message_id)

bot.polling()
