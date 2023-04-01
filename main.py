import datetime
import os
import urllib.parse

import requests
from dotenv import load_dotenv, find_dotenv














def main():

    load_dotenv(find_dotenv())

    try:
        nasa_token = os.environ['NASA_API']
    except KeyError:
        print('Не удается найти переменную окружения NASA_API')

    fetch_nasa_epic(nasa_token)


if __name__ == "__main__":
    main()