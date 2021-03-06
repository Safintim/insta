# insta

## Описание
С помощью данного кода можно скачать изображения последнего запуска SpaceX,
(а также изображения с телескопа Hubble), и загрузить в инстаграм. 

Использованные API:
* [Api Hubble](http://hubblesite.org/api/documentation)
* [Api SpaceX](https://documenter.getpostman.com/view/2025350/RWaEzAiG)
* [Github Api SpaceX](https://github.com/r-spacex/SpaceX-API)
## Требования

Для запуска скриптов требуется:

*Python 3.6*


## Как установить:

1. Установить Python3:

(Windows):[python.org/downloads](https://www.python.org/downloads/windows/)

(Debian):
```sh
sudo apt-get install python3
sudo apt-get install python3-pip
```
2. Установить зависимости и скачать сам проект:

```sh
git clone https://github.com/Safintim/insta.git
pip3 install -r requirements.txt
```

## Как использовать: 
Для скачивания картинок [Api SpaceX](https://documenter.getpostman.com/view/2025350/RWaEzAiG)
```sh
python3 fetch_space.py
```
Для скачивания картинок [Api Hubble](http://hubblesite.org/api/documentation)
```sh
python3 fetch_hubble.py
```

Для загрузки картинок в instagram
```sh
python3 upload_images.py
```

## Примеры:
Скачиваем картинки:
![Alt Text](http://ipic.su/img/img7/fs/insta1.1555686468.gif)

Загружаем картинки в instagram

![Alt Text](http://ipic.su/img/img7/fs/insta2.1555687771.gif)

## Комментарий: 
***
Все изображения сохраняются в папку images.
