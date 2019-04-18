from dotenv import load_dotenv
from instabot import Bot
import os


def upload_images():
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    bot = Bot()
    bot.login(username=login, password=password)
    image_path = 'images/'
    images = os.listdir(image_path)
    posted_images = set()
    for image in images:
        bot.upload_photo((image_path + image))
        if not bot.api.last_response.ok:
            continue
        posted_images.add(image)

    is_not_all_loaded = set(images).difference(posted_images)

    if is_not_all_loaded:
        print('These images were not uploaded: {}'.format(is_not_all_loaded))
