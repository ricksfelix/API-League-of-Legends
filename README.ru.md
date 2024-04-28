# API-Лига Легенд
API для получения изображений чемпионов

## Скачать репозиторий
```
git clone https://github.com/ricksfelix/API-League-of-Legends
```

## Установка зависимостей:
``` bash
pip install -r requirements.txt
```
## Обновление/загрузка изображений
Запустите [scrap.py](https://github.com/ricksfelix/API-League-of-Legends/blob/main/scrap.py)

На этом этапе он проверит [champ_list.txt](https://github.com/ricksfelix/API-League-of-Legends/blob/main/champ_list.txt), после чего проверит, нет ли даже одного изображения не хватает. После этого он загрузит изображения чемпионов.


```
python Scrap.py
```
## Полезная информация
- `Square` = значок чемпиона
- `Splash` = оригинальное знамя чемпиона.
- `Centered` = баннер, но с фокусом на чемпионе.
- `p` = пассивный значок
- `q` = Значок навыка "Q"
- `w` = значок навыка "W"
- `e` = значок навыка «E»
- `r` = значок навыка "R"

## выполнение API

> ## **СКОРО**

## Используемая документация:
  - [Communit Dragon](https://www.communitydragon.org/documentation)
  - [Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)
  - [io](https://docs.python.org/3/library/io.html#io.BytesIO)