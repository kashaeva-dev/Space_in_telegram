import argparse
import datetime
import os
import random
import time
from os.path import join

from dotenv import load_dotenv, find_dotenv

from bot import send_image
from file_processing import choose_images


def create_parser():
    parser = argparse.ArgumentParser(
        prog="""Send photos to channel""",
        description="""
        This script allows you sending images to a Telegram channel automatically.
        It mixed photos in the specifyed directory and sends all of them constantly
        in the given interval of time. By default it is 4 hours. You can also specify
        the directory of the images. By default it is "images".
        """,
    )
    parser.add_argument(
        '-h', '--hours',
        help="you can change the time interval in which the photos are to be sent",
        default=4,
        type=int,
    )
    parser.add_argument(
        '-d', '--directory',
        help='you can specify the directory of the images',
        default='images',
    )
    return parser


def main():
    parser = create_parser()
    user_input = parser.parse_args()

    hours = user_input.hours
    directory = user_input.directory

    load_dotenv(find_dotenv())

    try:
        tg_bot_token = os.environ['EPIC_SPACE_BOT_API']
        tg_chat_id = os.environ['TG_CHAT_ID']
    except KeyError:
        print('Не получается найти переменную окружения TG_CHAT_ID или EPIC_SPACE_BOT_API')
    else:
        while True:
            images = choose_images(directory)
            random.shuffle(images)
            for image in images:
                send_image(join(directory, image), tg_chat_id, tg_bot_token)
            time.sleep(datetime.timedelta(hours=hours).total_seconds())


if __name__ == "__main__":
    main()
