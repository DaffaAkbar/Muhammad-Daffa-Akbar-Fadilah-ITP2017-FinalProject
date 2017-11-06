import random
import pygame
import sys
from rulet_setting import Setting
from rulet_shoot_button import Shoot_Button
from rulet_button import Button
from rulet_function import*
from rulet_shoot_enemy_button import Shoot_Button_Enemy
from rulet_reroll import Reroll
from rulet_button_end import Button_end
from rulet_music import *
#bullet countdown that will get random at the start of the game
#The game end when the bullet hit zero
bullet = int(random.randint(1, 6))


#special action variable for each player that can only be done once each game
player1_reroll_limit=0
player2_reroll_limit=0
player1_shoot_enemy_limit=0
player2_shoot_enemy_limit=0

#A variable that determine which player will take action
round=1

#screen setting
setting=Setting()

#the background image
title_screen=pygame.image.load("title.jpg")
bg1 = pygame.image.load("player1.jpg")
bg2 = pygame.image.load("player2.jpg")
lose1=pygame.image.load("player1_lose.jpg")
lose2=pygame.image.load("player2_lose.jpg")


def rungame():
    pygame.init()
    global bullet

    #define the sound effect
    sound_shoot = pygame.mixer.Sound("shoot.wav")
    sound_reroll = pygame.mixer.Sound("reroll.wav")
    sound_empty= pygame.mixer.Sound("empty.wav")


    screen = pygame.display.set_mode([setting.width, setting.height])

    #make the game title
    pygame.display.set_caption("Russian Roulette")

    #make the play button
    play_button = Button(screen, "Play")

    #make the back button
    back_button=Button_end(screen, "Back")

    shoot_button = Shoot_Button(screen)
    shoot_button_enemy = Shoot_Button_Enemy(screen)
    reroll=Reroll(screen)

    # reroll button coordinate
    reroll_x1 = reroll.rect.left
    reroll_x2 = reroll.rect.right
    reroll_y1 = reroll.rect.top
    reroll_y2 = reroll.rect.bottom

    # shoot enemy button coordinate
    shoot_enemy_x1 = shoot_button_enemy.rect.left
    shoot_enemy_x2 = shoot_button_enemy.rect.right
    shoot_enemy_y1 = shoot_button_enemy.rect.top
    shoot_enemy_y2 = shoot_button_enemy.rect.bottom

    # shoot button coordinate
    shoot_x1 = shoot_button.rect.left
    shoot_x2 = shoot_button.rect.right
    shoot_y1 = shoot_button.rect.top
    shoot_y2 = shoot_button.rect.bottom

    game_active=False

    game_end=False

    while True:
        play_music()
        game_start(player1_shoot_enemy_limit, player2_shoot_enemy_limit, player1_reroll_limit,
                    player2_reroll_limit, sound_shoot, sound_reroll,sound_empty, round, bg1, bg2, screen,game_active,play_button,lose1,lose2,reroll_x1,reroll_x2,reroll_y1,reroll_y2,
                    shoot_x1, shoot_x2, shoot_y1, shoot_y2, shoot_enemy_x1, shoot_enemy_x2, shoot_enemy_y1,shoot_enemy_y2, back_button,game_end,title_screen
                    )

        end_game(player1_shoot_enemy_limit, player2_shoot_enemy_limit, player1_reroll_limit,
                    player2_reroll_limit, sound_shoot, sound_reroll,sound_empty, round, bg1, bg2, screen,game_active,play_button,lose1,lose2,reroll_x1,reroll_x2,reroll_y1,reroll_y2,
                    shoot_x1, shoot_x2, shoot_y1, shoot_y2, shoot_enemy_x1, shoot_enemy_x2, shoot_enemy_y1,shoot_enemy_y2, back_button,game_end,title_screen
                    )

rungame()

#Illustration done by Gunawan Budi
#This game is based on the alien invader that are provided in the python crash course