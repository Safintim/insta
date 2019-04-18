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
    for image in os.listdir(image_path):
        bot.upload_photo((image_path + image))
