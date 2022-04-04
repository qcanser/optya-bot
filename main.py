import time
import os
import telebot
import pandas
import schedule
import config
import feedparser

from multiprocessing import *
from telebot import types
from datetime import datetime
from time import mktime


bot = telebot.TeleBot(config.token)
group_id = os.environ.get('GROUP_ID')

today = datetime.now()
today_tuple = (today.month, today.day)


def start_process():
    p1 = Process(target=TimeSchedule.start_schedule, args=()).start()


class TimeSchedule():
    def start_schedule():
        schedule.every().day.at("13:51").do(TimeSchedule.send_congratulations)
        schedule.every().day.at("16:05").do(TimeSchedule.send_new_podcast)

        while True:
            schedule.run_pending()
            time.sleep(1)


    def send_congratulations():
        data = pandas.read_csv("birthdays.csv")
        birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
        if today_tuple in birthdays_dict:
            birthday_person = birthdays_dict[today_tuple]
            name = birthday_person["name"]
            bot.send_message(group_id, f"С Днём Рождения {name}! 🥳🥳🥳👋👋👋🔈🔈🔈🍺🍺🍺🍻🍻🍻😃😃😃")


    def send_new_podcast():
        podcast_url = feedparser.parse("https://promodj.com/strogonov-radioshow-technopolis/podcast.xml")
        podcast_link = podcast_url.entries[0]['link']

        for post in podcast_url.entries:
            pub_date = datetime.fromtimestamp(mktime(post.published_parsed)).strftime("%Y-%m-%d")
            today_date = ('2022-03-31')
            if today_date in pub_date:
                bot.send_message(group_id, f'🔥🔥🔥💯💯💯👍👍👍💪💪💪🙏🙏🙏 \n Свежий эфир радио-шоу "ТЕХНОПОЛИС" \n {podcast_link}')



@bot.message_handler(content_types=['image'])
def reply_genius(message):
    bot.send_message(message.chat.id, "Гениально 👍👍👍🔥🔥🔥🥰🥰🥰😃😃😃")


@bot.message_handler(regexp='Спасибо')
def reply_thanks(message):
    url = 'https://cs5.pikabu.ru/images/big_size_comm/2015-10_2/1444219702158350197.jpg'
    bot.send_photo(message.chat.id, url)


if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass