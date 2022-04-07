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
            

mas=[]
if os.path.exists('data/dialog.txt'):
    f=open('data/dialog.txt', 'r', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()


def answer(text):
    try:
        text=text.lower().strip()
        if os.path.exists('data/dialog.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'


@bot.message_handler(regexp='Артём как дела?')
def start(m, res=False):
    time.sleep(10)
    random_audio = open('audio/' + random.choice(os.listdir('audio')), 'rb')
    bot.send_audio(m.chat.id, random_audio) 
    audio.close()


@bot.message_handler(regexp='Когда соберёмся?')
def stop(message):
    time.sleep(10)
    bot.send_message(message.chat.id, 'Ребята у меня с 18 декабря отпуск . Я всё таки Вас соберу !')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if text is not mas:
        break
    else:
        time.sleep(10)
        f=open('data/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
        s=answer(message.text)
        f.write('u: ' + message.text + '\n' + s +'\n')
        f.close()
        bot.send_message(message.chat.id, s.capitalize())


@bot.message_handler(regexp='Когда выйдет новый эфир Технополис?')
def reply_new_podcast(message):
    time.sleep(10)
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
    time.sleep(10)
    random_answer = ['Гениально 👍👍👍🔥🔥🔥🥰🥰🥰😃😃😃', 
                    'Спасибо судья 👍🔥😊😊😊', 
                    'Гениально 👍👍👍👍👏👏👏😁😁😁',
                    'Спаси сохрани 🙏🙏🙏🤦‍♂️🤦‍♂️🤦‍♂️🤣🤣🤣',
                    'Я в шоке!!!🤦‍♂️🤦‍♂️🤦‍♂️🙏🙏🙏😃😃😃🔥🔥🔥🥰🥰🥰']
    bot.send_message(message.chat.id, random.choice(random_answer), reply_to_message_id=message.message_id)
    

@bot.message_handler(regexp='Лысый|Лысого|с лысым|у лысого|лысому')
def reply_thanks(message):
    time.sleep(10)
    video = open('file.mp4', 'rb')
    bot.send_video(message.chat.id, video, reply_to_message_id=message.message_id) 
    video.close()


@bot.message_handler(regexp='Едем|Едем!|Поедем?|Точно поедем?|Едешь?|Ты едешь?|Поехали?|едем|едем!|поедем?|точно поедем?|едешь?|ты едешь?|поехали?')
def reply_go(message):
    time.sleep(10)
    audio = open('audio/audio.ogg', 'rb')
    bot.send_audio(message.chat.id, audio, reply_to_message_id=message.message_id) 
    audio.close()


@bot.message_handler(content_types=["audio"])
def reply_audio(message):
    time.sleep(10)
    audio = open('audio/podcast.ogg', 'rb')
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