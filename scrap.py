import requests, os
from PIL import Image
from io import BytesIO

from rich import print

LINK = 'https://cdn.communitydragon.org/latest/champion/@name/@tag'
SQUARE = 'square'
SPLASH = 'splash-art'
CENTERED = 'splash-art/centered'
PORTRAIT = 'portrait'
P = 'ability-icon/p'
Q = 'ability-icon/q'
W = 'ability-icon/w'
E = 'ability-icon/e'
R = 'ability-icon/r'
FILE = 'champ_list.txt'

ALTER_NAMES = {
    'wukong':'monkeyking',
    'bardo':'bard'
}

def download_img(name, tag, img_type):
    if name in ALTER_NAMES: name = ALTER_NAMES[name]
    link_img = LINK.replace('@name', name).replace('@tag',tag)
    result = requests.get(link_img)
    save_dir = f'champions\\{name}\\{img_type}.png'

    if result.status_code == 200:
        img = Image.open(BytesIO(result.content))
        img.save(save_dir)
        
    if result.status_code == 404:
        print(f'[red]***\n({name}/{tag}) Não encontrado\n{link_img}\n***[/]')

def verify_and_download(name):
    verification = verify_champion(name)
    if not verification['square']: download_img(name, SQUARE, 'square') 
    if not verification['splash']: download_img(name, SPLASH, 'splash') 
    if not verification['centered']: download_img(name, CENTERED, 'centered') 
    if not verification['portrait']: download_img(name, PORTRAIT, 'portrait') 

    if not verification['p']: download_img(name, P, 'p') 
    if not verification['q']: download_img(name, Q, 'q') 
    if not verification['w']: download_img(name, W, 'w') 
    if not verification['e']: download_img(name, E, 'e') 
    if not verification['r']: download_img(name, R, 'r') 


def get_champion_name(file):
    champion_name = None
    with open(file, 'r') as file:
        champion_name = file.read()
        file.close()
    return champion_name.split('\n')


def verify_champion(name):
    if name in ALTER_NAMES: name = ALTER_NAMES[name]
    if not 'champions' in os.listdir(os.getcwd()): os.mkdir('champions')
    if not os.path.exists(f'{os.getcwd()}\\champions\\{name}'): os.mkdir(f'champions\\{name}')
    square = True if os.path.exists(f'{os.getcwd()}\\champions\\{name}\\square.png') else False
    splash = True if os.path.exists(f'{os.getcwd()}\\champions\\{name}\\splash.png') else False
    centered = True if os.path.exists(f'{os.getcwd()}\\champions\\{name}\\centered.png') else False
    portrait = True if os.path.exists(f'{os.getcwd()}\\champions\\{name}\\portrait.png') else False

    p = True if os.path.exists(f'{os.getcwd()}\\champions\\{name}\\p.png') else False
    q = True if os.path.exists(f'{os.getcwd()}\\champions\\{name}\\q.png') else False
    w = True if os.path.exists(f'{os.getcwd()}\\champions\\{name}\\w.png') else False
    e = True if os.path.exists(f'{os.getcwd()}\\champions\\{name}\\e.png') else False
    r = True if os.path.exists(f'{os.getcwd()}\\champions\\{name}\\r.png') else False

    verification = {
        'square': square,
        'splash': splash,
        'centered': centered,
        'portrait': portrait,
        'p':p,
        'q':q,
        'w':w,
        'e':e,
        'r':r
    }
    return verification

if __name__ == '__main__':
    for champion_name in get_champion_name(FILE):
        print(f'[yellow]{champion_name}[/]')
        verify_and_download(champion_name)
