import pygame
import threading
import os
import time

screen = None
picture = None
rect = None

lock = threading.Lock()

def init(kill):
    global screen

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    thread = threading.Thread(target=tick, args=(kill,))
    thread.start()
    return thread

def set(path):
    global picture, rect

    lock.acquire()
    picture = pygame.image.load(path)
    picture = pygame.transform.scale(picture, screen.get_size())
    rect = picture.get_rect()
    lock.release()
 
def tick(kill):
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True

        lock.acquire()
        if picture and rect:
            screen.blit(picture, rect)
        lock.release()

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    kill()
