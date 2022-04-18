import time
import os
import telebot
import pandas
import feedparser
import random
import schedule

from flask import Flask, request
from datetime import datetime
from time import mktime
from multiprocessing import *
from telebot import types
from fuzzywuzzy import fuzz

TOKEN = os.environ['BOT_API_TOKEN']
bot = telebot.TeleBot(TOKEN)
APP_URL = f'https://technopolis-bot.herokuapp.com/{TOKEN}'
group_id = os.environ['GROUP_ID']
server = Flask(__name__)


def start_process():
    p1 = Process(target=TimeSchedule.start_schedule, args=()).start()


class TimeSchedule():
    def start_schedule():
        schedule.every().day.at("04:00").do(TimeSchedule.send_congratulations)
        schedule.every().friday.at("05:00").do(TimeSchedule.send_new_podcast)


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
            print('Сегодня нет именинников.')


    def send_new_podcast():
        podcast_url = feedparser.parse("https://promodj.com/strogonov-radioshow-technopolis/podcast.xml")
        podcast_link = podcast_url.entries[0]['link']
        post_date = datetime.fromtimestamp(mktime(podcast_url.entries[0].published_parsed)).date()
        today_date = datetime.now().date()

        if today_date == post_date:
            bot.send_message(group_id, f'🔥🔥🔥💯💯💯👍👍👍💪💪💪🙏🙏🙏 \n Свежий эфир радио-шоу "ТЕХНОПОЛИС" \n \n {podcast_link}')
        else:
            print('Нет свежих эфиров.')


@bot.message_handler(regexp='Артём как дела?')
def start(message):
    random_audio = open('audio/' + random.choice(os.listdir('audio')), 'rb')
    bot.send_audio(message.chat.id, random_audio) 
    audio.close()


@bot.message_handler(regexp='Когда соберёмся?')
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


@bot.message_handler(regexp='Когда выйдет новый эфир Технополис?')
def reply_new_podcast(message):
    podcast_url = feedparser.parse("https://promodj.com/strogonov-radioshow-technopolis/podcast.xml")
    podcast_link = podcast_url.entries[0]['link']
    post_date = datetime.fromtimestamp(mktime(podcast_url.entries[0].published_parsed)).date()
    today_date = datetime.now().date()

    if today_date == post_date:
        bot.send_message(message.chat.id, f'🔥🔥🔥👍👍👍💯💯💯💪💪💪🥩🥩🥩 \n  Вот держи свежий эфир радио-шоу "ТЕХНОПОЛИС" \n \n {podcast_link}')
    else:
        bot.send_message(message.chat.id, 'Витя ещё не выложил 🤷🏻‍♂️') 


@bot.message_handler(content_types=["pinned_message", "photo", "voice", "video"])
def reply_genius(message):
    random_answer = [
                    'Гениально 👍👍👍🔥🔥🔥🥰🥰🥰😃😃😃',
                    'Спасибо судья 👍🔥😊😊😊', 
                    'Гениально 👍👍👍👍👏👏👏😁😁😁',
                    'Спаси сохрани 🙏🙏🙏🤦‍♂️🤦‍♂️🤦‍♂️🤣🤣🤣',
                    'Я в шоке!!!🤦‍♂️🤦‍♂️🤦‍♂️🙏🙏🙏😃😃😃🔥🔥🔥🥰🥰🥰'
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
    

@bot.message_handler(regexp='Лысый|Лысого|с лысым|у лысого|лысому')
def reply_thanks(message):
    video = open('file.mp4', 'rb')
    bot.send_video(message.chat.id, video, reply_to_message_id=message.message_id) 
    video.close()


@bot.message_handler(regexp='Едем|Едем!|Поедем?|Точно поедем?|Едешь?|Ты едешь?|Поехали?|едем|едем!|поедем?|точно поедем?|едешь?|ты едешь?|поехали?')
def reply_go(message):
    audio = open('audio/audio.ogg', 'rb')
    bot.send_audio(message.chat.id, audio, reply_to_message_id=message.message_id) 
    audio.close()


@bot.message_handler(content_types=["audio"])
def reply_audio(message):
    audio = open('podcast.ogg', 'rb')
    bot.send_audio(message.chat.id, audio, reply_to_message_id=message.message_id) 
    audio.close()


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    start_process()
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))