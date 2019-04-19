from dotenv import load_dotenv
from settings import IMAGE_PATH
from instabot import Bot
import os


def create_and_login_bot(login, password):
    bot = Bot()
    bot.login(username=login, password=password)
    return bot


def upload_images(bot):
    images = os.listdir(IMAGE_PATH)
    posted_images = set()
    for image in images:
        bot.upload_photo((IMAGE_PATH + image))
        if not bot.api.last_response.ok:
            continue
        posted_images.add(image)

    is_not_all_loaded = set(images).difference(posted_images)

    if is_not_all_loaded:
        print('These images were not uploaded: {}'.format(is_not_all_loaded))


def main():
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    bot = create_and_login_bot(login, password)
    upload_images(bot)


if __name__ == '__main__':
    main()
