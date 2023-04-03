import filetype
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


def is_correct_image(path):
    if os.path.isfile(path) and filetype.is_image(path) and os.stat(path).st_size < 20971520:
        return True


def choose_images(directory):
    images = []

    for image in os.listdir(directory):
        path = os.path.join(directory, image)
        if is_correct_image(path):
            images.append(image)
    return images
