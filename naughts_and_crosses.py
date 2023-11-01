import pygame

SCREEN_RESOLOUTION = (1280, 720)

def start_game():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_RESOLOUTION)
    clock = pygame.time.Clock()
