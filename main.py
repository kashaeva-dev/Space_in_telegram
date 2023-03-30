import requests
import os


def get_image(url, path):

    response = requests.get(url)
    response.raise_for_status()

    directory, filename = path.split('/')
    os.makedirs(directory, exist_ok=True)

    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch(flight_id='61eefaa89eb1064137a1bd73'):

    response = requests.get(f'https://api.spacexdata.com/v5/launches/{flight_id}')

    links = response.json()['links']['flickr']['original']

    for index, link in enumerate(links):
        get_image(link, f'images/spacex_{index}')


if __name__ == "__main__":
    fetch_spacex_launch()
