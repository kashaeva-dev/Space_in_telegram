import argparse
import datetime
import os
import random
import time
from os import listdir
from os.path import isfile, join

import telegram

from environment import get_bot_token, get_chat_id


def send_message(text, chat_id, token):
    bot = telegram.Bot(token)
    bot.send_message(text=text, chat_id=chat_id)


def send_image(path, chat_id, token):
    bot = telegram.Bot(token=token)
    bot.send_document(chat_id=chat_id, document=open(path, 'rb'), timeout=100)


def create_parser():
    parser = argparse.ArgumentParser(
        prog="""Send photos to channel""",
        description="""
        This script allows you sending images to a Telegram channel automatically.
        It mixed photos in the specifyed directory and sends all of them constantly
        in the given interval of time. By default it is 4 hours. You can also specify
        the directory of the images. By default it is "images".
        """
    )
    parser.add_argument(
        'hours',
        help="you can change the time interval in which the photos are to be sent",
        default=4,
        type=int,
    )
    parser.add_argument(
        '-d', '--directory',
        help='you can specify the directory of the images',
        default='images'
    )
    return parser

def main():
    parser = create_parser()
    user_input = parser.parse_args()

    hours = user_input.hours
    directory = user_input.directory

    files=[]

    for file in listdir(directory):
        path = join(directory, file)
        if isfile(path) and os.stat(path).st_size < 20971520:
            files.append(file)

    bot_token = get_bot_token()
    chat_id = get_chat_id()
    if bot_token and chat_id:
        while True:
            random.shuffle(files)
            for file in files:
                send_image(join(directory, file), chat_id, bot_token)
            time.sleep(datetime.timedelta(hours=hours).total_seconds())


if __name__ == "__main__":
    main()
