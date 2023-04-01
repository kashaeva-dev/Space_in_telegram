import requests
import os
import urllib


def get_image(url, path):

    response = requests.get(url)
    response.raise_for_status()

    directory, filename = os.path.split(os.path.splitext(path)[0])
    os.makedirs(directory, exist_ok=True)

    with open(path, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    path = urllib.parse.urlsplit(url).path
    return os.path.splitext(path)[1]
