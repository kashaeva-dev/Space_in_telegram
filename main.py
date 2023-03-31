import datetime
import os
import urllib.parse

import requests
from dotenv import load_dotenv, find_dotenv


def get_image(url, path):

    response = requests.get(url)
    response.raise_for_status()

    directory, filename = os.path.split(os.path.splitext(path)[0])
    os.makedirs(directory, exist_ok=True)

    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch(flight_id='61eefaa89eb1064137a1bd73'):

    url = f'https://api.spacexdata.com/v5/launches/{flight_id}'
    launch_data = requests.get(url)
    launch_data.raise_for_status()

    urls = launch_data.json()['links']['flickr']['original']

    for index, url in enumerate(urls):
        extension = get_file_extension(url)
        get_image(url, f'images/spacex_{index}{extension}')


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
            urls.append(photo['hdurl'])

    for index, url in enumerate(urls):
        extension = get_file_extension(url)
        try:
            get_image(url, f'images/nasa_apod_{index}{extension}')
        except requests.exceptions.HTTPError:
            continue


def get_file_extension(url):
    path = urllib.parse.urlsplit(url).path
    return os.path.splitext(path)[1]


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

        url = f'https://api.nasa.gov/EPIC/archive/natural/{yesterday.year}/{yesterday.month:02d}/{yesterday.day}/png/{id}.png?api_key={token}'
        get_image(url, f'images/nasa_epic_{index}.png')


def main():

    load_dotenv(find_dotenv())

    try:
        nasa_token = os.environ['NASA_API']
    except KeyError:
        print('Не удается найти переменную окружения NASA_API')

    fetch_nasa_epic(nasa_token)


if __name__ == "__main__":
    main()