import argparse
import datetime
import os

import requests
from dotenv import load_dotenv, find_dotenv

from file_processing import get_image


def fetch_nasa_epic(token):

    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)

    request_url = f'https://api.nasa.gov/EPIC/api/natural/date/{yesterday.strftime("%Y-%m-%d")}'

    params = {
        'api_key': token,
    }

    response = requests.get(request_url, params=params)
    response.raise_for_status()

    epic_photos_metadata = response.json()
    epic_ids = []
    for epic in epic_photos_metadata:
        epic_ids.append(epic['image'])

    for index, image_id in enumerate(epic_ids):

        url = f'https://api.nasa.gov/EPIC/archive/natural/' \
              f'{yesterday.year}/{yesterday.month:02d}/{yesterday.day:02d}/png/{image_id}.png'
        get_image(url, params, f'images/nasa_epic_{index}.png')


def main():
    load_dotenv(find_dotenv())

    try:
        nasa_api_token = os.environ['NASA_API_TOKEN']
    except KeyError:
        print('Не получается найти переменную окружения NASA_API_TOKEN')
    else:
        fetch_nasa_epic(nasa_api_token)


if __name__ == "__main__":
    main()
