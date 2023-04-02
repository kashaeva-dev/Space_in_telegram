import argparse
import datetime

import requests
from environment import get_nasa_token

from file_processing import get_image


def fetch_nasa_epic(token):

    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)

    request_url = f'https://api.nasa.gov/EPIC/api/natural/date/{yesterday.strftime("%Y-%m-%d")}?api_key={token}'
    response = requests.get(request_url)
    response.raise_for_status()

    epic_photo_information = response.json()
    epic_ids = []
    for photo in epic_photo_information:
        epic_ids.append(photo['image'])

    for index, id in enumerate(epic_ids):

        url = f'https://api.nasa.gov/EPIC/archive/natural/{yesterday.year}/{yesterday.month:02d}/{yesterday.day:02d}/png/{id}.png?api_key={token}'
        get_image(url, f'images/nasa_epic_{index}.png')


def create_parser():

    parser = argparse.ArgumentParser(
        prog='NASA EPIC images',
        description='The "NASA EPIC images" program allows you to download '
             'EPIC Earth images that were made yesterday',
    )
    return parser


def main():
    parser = create_parser()
    user_input = parser.parse_args()

    nasa_token = get_nasa_token()

    if nasa_token:
        fetch_nasa_epic(nasa_token)


if __name__ == "__main__":
    main()
