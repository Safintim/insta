import requests
import pathlib
from settings import IMAGE_PATH


def get_file_extension(file_url):
    return file_url.split('.')[-1]


def download_and_save_image(url, filename):

    pathlib.Path(IMAGE_PATH).mkdir(exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(IMAGE_PATH+filename, 'wb') as f:
        f.write(response.content)
