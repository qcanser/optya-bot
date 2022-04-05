import time
import os
import telebot
import pandas
import feedparser

from telebot import types
from datetime import datetime
from time import mktime

token = os.environ['BOT_API_TOKEN']
bot = telebot.TeleBot(token)
group_id = os.environ['GROUP_ID']


def send_congratulations():
    data = pandas.read_csv("birthdays.csv")
    today = datetime.now()
    today_tuple = (today.month, today.day)
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

    if today_tuple in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        name = birthday_person["name"]
        bot.send_message(group_id, f"С Днём Рождения {name}! 🥳🥳🥳👋👋👋🔈🔈🔈🍺🍺🍺🍻🍻🍻😃😃😃")


def send_new_podcast():
    podcast_url = feedparser.parse("https://promodj.com/strogonov-radioshow-technopolis/podcast.xml")
    podcast_link = podcast_url.entries[0]['link']
    today = datetime.now()
    
    for post in podcast_url.entries:
        post_date = datetime.fromtimestamp(mktime(post.published_parsed)).strftime("%Y-%m-%d")
        today_date = today.strftime("%Y-%m-%d")
        if today_date in post_date:  
            bot.send_message(group_id, f'🔥🔥🔥💯💯💯👍👍👍💪💪💪🙏🙏🙏 \n Свежий эфир радио-шоу "ТЕХНОПОЛИС" \n \n {podcast_link}')


@bot.message_handler(content_types=["sticker", "pinned_message", "photo", "audio", "voice", "video"])
def reply_genius(message):
    time.sleep(10)
    bot.send_message(message.chat.id, "Гениально 👍👍👍🔥🔥🔥🥰🥰🥰😃😃😃")


# @bot.message_handler(regexp='Спасибо')
# def reply_thanks(message):
#     time.sleep(10)
#     video = open('file.mp4', 'rb')
#     bot.send_video(message.chat.id, video) 
#     video.close()


if __name__ == '__main__':
    start_process()
    bot.polling(none_stop=True)
