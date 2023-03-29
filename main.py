import requests
import os


def get_image(url, path):

    response = requests.get(url)
    response.raise_for_status()

    directory, filename = path.split('/')
    os.makedirs(directory, exist_ok=True)

    with open(path, 'wb') as file:
        file.write(response.content)


def get_images_links(id):

    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')

    return response.json()['links']['flickr']['original']


if __name__ == "__main__":

    id = '61eefaa89eb1064137a1bd73'

  #  for index, link in enumerate(get_image_links(id)):
  #      get_image(link)
    print(get_images_links(id))
