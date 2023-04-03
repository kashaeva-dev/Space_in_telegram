import argparse

import requests

from file_processing import get_image, get_file_extension


def fetch_spacex_launch(flight_id):

    url = f'https://api.spacexdata.com/v5/launches/{flight_id}'
    launch_data = requests.get(url)
    launch_data.raise_for_status()

    urls = launch_data.json()['links']['flickr']['small']

    if urls:
        for index, url in enumerate(urls):
            extension = get_file_extension(url)
            get_image(url, f'images/spacex_{index}{extension}')
    else:
        print("There is no images for requested flight")


def create_parser():
    parser = argparse.ArgumentParser(
        prog='SpaceX launch images',
        description='The "SpaceX launch images" program allows you to download images '
                    'of SpaceX launches. You can either specify the ID of a particular'
                    ' launch or retrieve photos from the latest launch without specifying'
                    'any ID.',
    )
    parser.add_argument(
        '-id', '--flight_id',
        help='You can specify the ID of a particular launch',
        default='latest',
    )
    return parser


def main():
    parser = create_parser()
    user_input = parser.parse_args()

    flight_id = user_input.flight_id

    fetch_spacex_launch(flight_id)


if __name__ == "__main__":
    main()
