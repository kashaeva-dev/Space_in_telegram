import urllib.parse

import requests
import os


def get_image(url, path):

    response = requests.get(url)
    response.raise_for_status()

    directory, filename = os.path.split(os.path.splitext(path)[0])
    os.makedirs(directory, exist_ok=True)

    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch(flight_id='61eefaa89eb1064137a1bd73'):

    response = requests.get(f'https://api.spacexdata.com/v5/launches/{flight_id}')

    links = response.json()['links']['flickr']['original']

    for index, link in enumerate(links):
        get_image(link, f'images/spacex_{index}.jpg')


def get_file_extension(url):
    path = urllib.parse.urlsplit(url).path
    return os.path.splitext(path)[1]


if __name__ == "__main__":
    print(get_file_extention('https://example.com/txt/hello%20world.txt?v=9#python'))