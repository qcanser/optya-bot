from datetime import datetime
import time
import os
import telebot
import pandas
import schedule
import config
import feedparser

from multiprocessing import *
from telebot import types


bot = telebot.TeleBot(config.token)
group_id = os.environ.get('GROUP_ID')

today = datetime.now()
today_tuple = (today.month, today.day)


def start_process():
    p1 = Process(target=TimeSchedule.start_schedule, args=()).start()


class TimeSchedule():
    def start_schedule():
        schedule.every().day.at("04:00").do(TimeSchedule.send_congratulations)
        schedule.every().day.at("04:01").do(TimeSchedule.send_new_podcast)

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
        d = feedparser.parse("https://promodj.com/strogonov-radioshow-technopolis/podcast.xml")
        podcast_link = d.entries[0]['link']
        bot.send_message(group_id, f'🔥🔥🔥💯💯💯👍👍👍💪💪💪🙏🙏🙏 \n Свежий эфир радио-шоу "ТЕХНОПОЛИС" \n {podcast_link}')


if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass