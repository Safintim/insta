import requests
import pathlib


def get_file_extension(file_url):
    return file_url.split('.')[-1]


def get_picture(url, filename):

    directory = 'images/'
    pathlib.Path(directory).mkdir(exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(directory+filename, 'wb') as f:
        f.write(response.content)


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v3/launches/latest'

    response = requests.get(api_url)
    response.raise_for_status()

    pictures = response.json()['links']['flickr_images']
    for i, image_url in enumerate(pictures):
        filename = 'spacex{}.{}'.format(i, get_file_extension(image_url))
        get_picture(image_url, filename)
