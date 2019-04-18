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
    filename = 'images/spacex{}.'

    response = requests.get(api_url).json()
    pictures = response['links']['flickr_images']
    for i, image_url in enumerate(pictures):
        extension = get_file_extension(image_url)
        new_filename = filename.format(i) + extension
        get_picture(image_url, new_filename)


def fetch_hubble_once_image(image_id):
    image_id_url = 'http://hubblesite.org/api/v3/image/{}'
    filename = 'images/hubble{}.'.format(image_id)
    response = requests.get(image_id_url.format(image_id)).json()
    last_image_url = response['image_files'][-1]['file_url']
    extension = get_file_extension(last_image_url)
    new_filename = filename + extension
    get_picture(last_image_url, new_filename)


def fetch_hubble(collection='wallpaper'):
    collection_url = 'http://hubblesite.org/api/v3/images/{}'.format(collection)

    response = requests.get(collection_url).json()
    for image in response:
        fetch_hubble_once_image(image['id'])


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
