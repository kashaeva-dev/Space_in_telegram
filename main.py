import requests
import os


def get_image(url, path):

    response = requests.get(url)
    response.raise_for_status()

    directory, filename = path.split('/')
    os.makedirs(directory, exist_ok=True)

    with open(path, 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    path = 'images/hubble.jpg'
    get_image(url, path)
