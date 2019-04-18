import requests
import pathlib


def get_file_extension(file_url):
    return file_url.split('.')[-1]


def get_picture(url, path):

    pathlib.Path('images').mkdir(exist_ok=True)
    response = requests.get(url)

    with open(path, 'wb') as f:
        f.write(response.content)


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v3/launches/latest'

    response = requests.get(api_url).json()
    pictures = response['links']['flickr_images']
    for i, image_url in enumerate(pictures):
        filename = 'images/spacex{}.'.format(i) + get_file_extension(image_url)
        get_picture(image_url, filename)
