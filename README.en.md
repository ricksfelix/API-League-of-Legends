# API-League-of-Legends
API to get images of champions

## Download repository
```
git clone https://github.com/ricksfelix/API-League-of-Legends
```

## Installation of Dependencies:
```bash
pip install -r requirements. txt
```
## Update/Download Images
Run [scrap.py](https://github.com/ricksfelix/API-League-of-Legends/blob/main/scrap.py)

In this step, it will check the [champ_list.txt](https://github.com/ricksfelix/API-League-of-Legends/blob/main/champ_list.txt), after that it will check if there is not even one image missing . After that it will download the images of the champions.


```
python scrap.py
```
## Useful information
- `Square` = Champion icon
- `Splash` = Champion's Original Banner
- `Centered` = Banner but focusing on the champion
- `p` = Passive Icon
- `q` = Icon of the skill "Q"
- `w` = Icon of the skill "W"
- `e` = Icon of the skill "E"
- `r` = Icon of the skill "R"


## API execution

> ## **COMING SOON**

## Documentation Used:
  - [Communit Dragon](https://www.communitydragon.org/documentation)
  - [Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)
  - [io](https://docs.python.org/3/library/io.html#io.BytesIO)