import argparse
import os
import random

from dotenv import load_dotenv, find_dotenv

from bot import send_image
from file_processing import choose_images, is_correct_image


def create_parser():
    parser = argparse.ArgumentParser(
        prog="Send one photo to a Telegram channel",
        description="""The scrip allows you to send one specifyed photo to a Telegram channel.
        If no photo specifyed it sends a random photo from "images" directory.
        """,
    )
    parser.add_argument(
        '-f', '--filename',
        help="you can define particular photo in the 'image' directory to be sent",
    )
    return parser


def main():
    parser = create_parser()
    filename = parser.parse_args().filename

    if filename and is_correct_image(os.path.join('images', filename)):
        path = os.path.join('images', filename)
    else:
        images = choose_images('images')
        path = os.path.join('images', random.choice(images))

    load_dotenv(find_dotenv())

    try:
        tg_bot_token = os.environ['TG_EPIC_SPACE_BOT_API']
        tg_chat_id = os.environ['TG_CHAT_ID']
    except KeyError:
        print('Не получается найти переменную окружения TG_CHAT_ID или TG_EPIC_SPACE_BOT_API')
    else:
        send_image(path, tg_chat_id, tg_bot_token)


if __name__ == "__main__":
    main()
