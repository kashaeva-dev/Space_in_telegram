import os
from dotenv import load_dotenv, find_dotenv

def get_nasa_token():

    load_dotenv(find_dotenv())

    try:
        nasa_token = os.environ['NASA_API']
    except KeyError:
        print('Не получается найти переменную окружения NASA_API')

    return nasa_token