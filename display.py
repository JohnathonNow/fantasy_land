import pygame
import threading
import os
import time

screen = None
picture = None

def get():
    return picture

def get_js():
    return """
    <style>html,body{{margin:0; height:100%;}}img{{display:block; width:100%; height:100%; object-fit: cover;}}</style>
    <img src=\"{}\" style=\"height:100%;width:100%;\" id=\"img\">
    <script>var i = 0;function a(){{document.getElementById('img').src = window.location.href + 'bg?d='+i; i++; }}a();setInterval(a, 1000);</script>
    """.format(picture)

def set(path):
    global picture
    picture = path
