import requests

def get_flights_with_photo_ids():

    """Сохраняет список id полетов с датами и количестом фотографий"""

    response = requests.get(f'https://api.spacexdata.com/v5/launches/')
    spaceX_data = response.json()

    ids = []
    for flight in spaceX_data:
        if flight['links']['flickr']['original']:
            ids.append("-".join([flight['id'],
                                 flight['date_local'],
                                 str(len(flight['links']['flickr']['original'])),
                                 ]
                                )
                       )

    with open('launches.txt', 'w') as file:
        file.write(" ".join(ids))