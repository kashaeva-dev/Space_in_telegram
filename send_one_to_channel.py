import argparse
import os
import random

from environment import get_bot_token, get_chat_id
from bot import send_image
from file_processing import choose_images, is_correct_image


def create_parser():
    parser = argparse.ArgumentParser(
        prog="Send one photo to a Telegram channel",
        description="""The scrip allows you to send one specifyed photo to a Telegram channel.
        If no photo specifyed it sends a random photo from "images" directory.
        """
    )
    parser.add_argument(
        '-f', '--filename',
        help="you can define particular photo in the 'image' directory to be sent",
    )
    return parser

def main():
    bot_token = get_bot_token()
    chat_id = get_chat_id()

    parser = create_parser()
    filename = parser.parse_args().filename

    if filename and is_correct_image(os.path.join('images', filename)):
        path = os.path.join('images', filename)
    else:
        images = choose_images('images')
        path = os.path.join('images', random.choice(images))

    if bot_token and chat_id:
        print(f"Отправляю фото {path}")
        send_image(path, chat_id, bot_token)


if __name__ == "__main__":
    main()