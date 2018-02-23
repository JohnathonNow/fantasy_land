import yaml
import time
import player
import display

CONFIG = None
PAGE = None

MAIN_PAGE_HEADER  = "<html><body><h1>Scenes</h1><br>"
MAIN_PAGE_ELEMENT = "<h2>{0}</h2><a href=\"/scene/{0}\"><img src=\"./{1}\" style=\"height:200px;\"></a><br>"
MAIN_PAGE_FOOTER  = "</body><html>"

SCENE_PAGE_HEADER  = "<html><body><h1>{}</h1><br>"
SCENE_PAGE_ELEMENT = "<a href=\"/scene/{1}/{0}\"><h2>{0}</h2></a><br>"
SCENE_PAGE_FOOTER  = "</body><a href=\"/\"><u>back</u></a><html>"

def load_config(config):
    global CONFIG, PAGE
    with open(config) as f:
        try:
            CONFIG = yaml.load(f)
            toadd = [MAIN_PAGE_HEADER]
            for title in CONFIG:
                scene = CONFIG[title]
                toadd.append(MAIN_PAGE_ELEMENT.format(title, scene['image']))
            toadd.append(MAIN_PAGE_FOOTER)
            PAGE = ''.join(toadd)
        except yaml.YAMLError as e:
            print('Error loading config file, {}'.format(e))

def get_main():
    return PAGE

def get_scene(scene):
    display.set(CONFIG[scene]['image'])
    toadd = [SCENE_PAGE_HEADER.format(scene)]
    for title in CONFIG[scene]['moods']:
        toadd.append(SCENE_PAGE_ELEMENT.format(title, scene))
    toadd.append(SCENE_PAGE_FOOTER)
    return ''.join(toadd)

def get_mood(scene, mood):
    player.play(CONFIG[scene]['moods'][mood]['music'])
    toadd = [SCENE_PAGE_HEADER.format(scene)]
    for title in CONFIG[scene]['moods']:
        toadd.append(SCENE_PAGE_ELEMENT.format(title, scene))
    toadd.append(SCENE_PAGE_FOOTER)
    return ''.join(toadd)

def debug():
    print(CONFIG)
