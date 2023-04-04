import argparse
import os

import requests
from dotenv import load_dotenv, find_dotenv

from file_processing import get_image, get_file_extension


def fetch_nasa_apod(token, count=50):

    request_url = 'https://api.nasa.gov/planetary/apod'

    params = {
        "count": count,
        "api_key": token,
    }

    photo_data = requests.get(request_url, params=params)
    photo_data.raise_for_status()

    urls = []
    for photo in photo_data.json():
        if photo['media_type'] == 'image':
            urls.append(photo['url'])

    for index, url in enumerate(urls):
        extension = get_file_extension(url)
        """Without this try-except block program is interrupted if it is impossible to get the image"""
        try:
            get_image(url, f'images/nasa_apod_{index}{extension}')
        except requests.exceptions.HTTPError:
            continue


def create_parser():
    parser = argparse.ArgumentParser(
        prog="NASA APOD images",
        description='The "NASA APOD images" program allows you to download '
                    'the specifyed number of images from Astronomy Picture of the Day '
                    'website',
    )
    parser.add_argument(
        '-c', '--count',
        help='You can specify the number of photos you want to be downloaded, by default it is 5',
        default=5,
        type=int,
    )
    return parser


def main():
    parser = create_parser()
    user_input = parser.parse_args()

    count = user_input.count

    load_dotenv(find_dotenv())

    try:
        nasa_api_token = os.environ['NASA_API']
    except KeyError:
        print('Не получается найти переменную окружения NASA_API')
    else:
        fetch_nasa_apod(nasa_api_token, count)


if __name__ == "__main__":
    main()
