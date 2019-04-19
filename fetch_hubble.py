import requests
from settings import get_file_extension, download_and_save_image


def fetch_hubble_once_image(image_id):
    image_id_url = 'http://hubblesite.org/api/v3/image/{}'
    response = requests.get(image_id_url.format(image_id))
    response.raise_for_status()

    last_image_url = response.json()['image_files'][-1]['file_url']
    filename = 'hubble{}.{}'.format(image_id, get_file_extension(last_image_url))
    get_picture(last_image_url, filename)


def fetch_hubble(collection='wallpaper'):
    collection_url = 'http://hubblesite.org/api/v3/images/{}'.format(collection)

    response = requests.get(collection_url)
    response.raise_for_status()

    for image in response.json():
        fetch_hubble_once_image(image['id'])
