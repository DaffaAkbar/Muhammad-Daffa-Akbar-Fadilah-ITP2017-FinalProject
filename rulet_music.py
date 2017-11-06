import pygame
def play_music():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

