import os
from dotenv import load_dotenv, find_dotenv


def get_nasa_token():
    load_dotenv(find_dotenv())

    try:
        nasa_token = os.environ['NASA_API']
        return nasa_token
    except KeyError:
        print('Не получается найти переменную окружения NASA_API')


def get_bot_token():
    load_dotenv(find_dotenv())

    try:
        bot_token = os.environ['EPIC_SPACE_BOT_API']
        return bot_token
    except KeyError:
        print('Не получается найти переменную окружения EPIC_SPACE_BOT_API')


def get_chat_id():
    load_dotenv(find_dotenv())

    try:
        bot_token = os.environ['CHAT_ID']
        return bot_token
    except KeyError:
        print('Не получается найти переменную окружения CHAT_ID')
