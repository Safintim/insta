import requests
from settings import get_file_extension, download_and_save_image


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v3/launches/latest'

    response = requests.get(api_url)
    response.raise_for_status()

    pictures = response.json()['links']['flickr_images']
    for i, image_url in enumerate(pictures):
        filename = 'spacex{}.{}'.format(i, get_file_extension(image_url))
        download_and_save_image(image_url, filename)
