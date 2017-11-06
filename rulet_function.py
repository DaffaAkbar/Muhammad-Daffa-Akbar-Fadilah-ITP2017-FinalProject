import sys
import random
import pygame

#A function to draw the main menu
def draw_title(play_button,title_screen,screen):
    screen.blit(title_screen,  (0, 0))
    play_button.draw_button()
    pygame.display.flip()

#a function at the end of the game
def end_game(player1_shoot_enemy_limit, player2_shoot_enemy_limit, player1_reroll_limit,
                    player2_reroll_limit, sound_shoot, sound_reroll,sound_empty, round, bg1, bg2, screen,game_active,play_button,lose1,lose2,reroll_x1,reroll_x2,reroll_y1,reroll_y2,
                    shoot_x1, shoot_x2, shoot_y1, shoot_y2, shoot_enemy_x1, shoot_enemy_x2, shoot_enemy_y1,shoot_enemy_y2, back_button,game_end,title_screen
                    ):

    #draw the back button
    back_button.draw_button()
    pygame.display.flip()

    #only run when game_end is False
    while game_end==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #to get the mouse position
            elif event.type == pygame.MOUSEBUTTONDOWN:
               mouse_x, mouse_y = pygame.mouse.get_pos()
               end_clicked = back_button.rect.collidepoint(mouse_x, mouse_y)
               if end_clicked:
                   #if the back button is clicked than the game start function will run again
                        game_start(player1_shoot_enemy_limit, player2_shoot_enemy_limit, player1_reroll_limit,
                                    player2_reroll_limit, sound_shoot, sound_reroll, sound_empty, round, bg1, bg2,
                                    screen, game_active,
                                    play_button, lose1, lose2, reroll_x1, reroll_x2, reroll_y1, reroll_y2, shoot_x1,
                                    shoot_x2, shoot_y1, shoot_y2, shoot_enemy_x1, shoot_enemy_x2, shoot_enemy_y1,
                                    shoot_enemy_y2, back_button, game_end,title_screen)

#The function that handle the whole system
def game_start(player1_shoot_enemy_limit,player2_shoot_enemy_limit,player1_reroll_limit,player2_reroll_limit,sound_shoot,sound_reroll,sound_empty,round,bg1,bg2,screen,game_active,
                play_button,lose1,lose2,reroll_x1,reroll_x2,reroll_y1,reroll_y2,shoot_x1,shoot_x2,shoot_y1,shoot_y2,shoot_enemy_x1,shoot_enemy_x2,shoot_enemy_y1,
                shoot_enemy_y2,back_button,game_end,title_screen):

    # everytime the game begin the bullet will randomize
    bullet =random.randint(1,6)

    #this function will only run when bullet is greater than 0

    while bullet>0:
        for event in pygame.event.get():
            #at the start of the game the game will not yet be initiate but instead will go to the main menu first
            if game_active==False:
            #drawing the main menu
                draw_title(play_button,title_screen,screen)

            #if ypu click exit button on the top right corner the the game will quit
            if event.type == pygame.QUIT:
                sys.exit()

            #to get the mouse position
            elif event.type == pygame.MOUSEBUTTONDOWN:
               mouse_x, mouse_y = pygame.mouse.get_pos()

               #the game start with game_active variable False
               if game_active==False:

                   #An action will only run if a player click on one of the action button
                    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
                    print(game_active)

                    #the game only run when a player click the play button and game_active become True
                    if mouse_x > shoot_enemy_x1 and mouse_x < shoot_enemy_x2 and mouse_y > shoot_enemy_y1 and mouse_y < shoot_enemy_y2 or button_clicked:

                        game_active=True

                        if bullet>0:
                            screen.blit(bg1, (0, 0))
                            pygame.display.flip()

                    #quit button location at the title screen
                    if mouse_x > reroll_x1 and mouse_x < reroll_x2 and mouse_y > reroll_y1 and mouse_y < reroll_y2:
                        sys.exit()

                        #this function only start when game_active become True
               if game_active==True:

                    #posisiton for the shoot button
                   if mouse_x>shoot_x1 and mouse_x<shoot_x2 and mouse_y>shoot_y1 and mouse_y<shoot_y2:
                   #shoot button action
                   #everytime round variable become an even number then it is player 2 turn
                        if round%2==0:

                            # everytime this action is initiate, the number of bullet will decrease
                            bullet = bullet-1

                            #everytime this action is initiate, the number of round will increase
                            round = round+1

                            print(bullet)
                            print(round)

                            if bullet>0:
                                pygame.mixer.Sound.play(sound_empty)
                                screen.blit(bg1, (0, 0))
                                pygame.display.flip()

                            #when palyer 2 initiate this action and the bullet become zero then player 2 will die
                            if bullet == 0 :
                                screen.blit(lose2,(0,0))
                                pygame.display.flip()
                                pygame.mixer.Sound.play(sound_shoot)

                        else:
                            # everytime this action is initiate, the number of bullet will decrease
                            bullet = bullet - 1

                            # everytime this action is initiate, the number of round will increase
                            round = round + 1

                            print(bullet)
                            print(round)

                            if bullet>0:
                                pygame.mixer.Sound.play(sound_empty)
                                screen.blit(bg2, (0, 0))
                                pygame.display.flip()

                            # when player 1 initiate this action and the bullet become zero then player 1 will die

                            if bullet==0 and round%2==0:
                                screen.blit(lose1,(0, 0))
                                pygame.display.flip()
                                pygame.mixer.Sound.play(sound_shoot)

                        #shoot enemy limit button position
                   if mouse_x > shoot_enemy_x1 and mouse_x < shoot_enemy_x2 and mouse_y > shoot_enemy_y1 and mouse_y < shoot_enemy_y2:

                   #shoot enemy limit for player 2
                   # as for the player 2,when the round hit even number than it is player 2 turn
                        if player2_shoot_enemy_limit == 0 and round%2 == 0:

                            # everytime this action is initiate, the number of bullet will decrease
                            bullet = bullet - 1

                            # everytime  player 2 take this action, the number of round will increase
                            round = round+1

                            # shoot enemy can only be initiate once
                            player2_shoot_enemy_limit = player2_shoot_enemy_limit+1


                            if bullet>0:
                                pygame.mixer.Sound.play(sound_empty)
                                screen.blit(bg1,(0,0))
                                pygame.display.flip()

                            #if the bullet countdown reach zero than the enemy will die
                            if bullet==0:
                                screen.blit(lose1,(0, 0))
                                pygame.display.flip()
                                pygame.mixer.Sound.play(sound_shoot)

                        # if the player had done this action before then it cannot be initiate again
                        elif player2_shoot_enemy_limit == 1 and round%2 == 0:
                            print("you cannot do this again")

                        #shoot enemy limit for player 1
                        elif player1_shoot_enemy_limit == 0:

                            #everytime this action is initiate, the number of bullet will decrease
                            bullet = bullet - 1

                            # everytime  player 1 take this action, the number of round will increase
                            round = round + 1

                            #shoot enemy can only be initiate once
                            player1_shoot_enemy_limit = player1_shoot_enemy_limit + 1

                            print(bullet)
                            print(round)

                            if bullet>0:
                                pygame.mixer.Sound.play(sound_empty)
                                screen.blit(bg2, (0, 0))
                                pygame.display.flip()

                            #if the bullet countdown reach zero then the enemy will die
                            if bullet == 0:
                                screen.blit(lose2, (0, 0))
                                pygame.display.flip()
                                pygame.mixer.Sound.play(sound_shoot)


                        #if the player had done this action before then it cannot be initiate again
                        elif player1_shoot_enemy_limit == 2:
                            print("you cannot do this again")

                        #reroll button position
                   if mouse_x > reroll_x1 and mouse_x < reroll_x2 and mouse_y > reroll_y1 and mouse_y < reroll_y2:

                        #reroll limit for player 2
                        #as for the player 2,when the round hit even number than it is player 2 turn
                        if player2_reroll_limit == 0 and round%2 == 0:

                            # everytime reroll is activate, the reroll sound will activate
                            pygame.mixer.Sound.play(sound_reroll)

                            # If player initiate reroll then the bullet will randomly place again betwenn 1 and 6
                            bullet=random.randint(1,6)

                            # reroll limit is once per game
                            player2_reroll_limit += 1

                            # everytime a player take action, the number of round will increase
                            round=round+1

                            screen.blit(bg1, (0, 0))
                            pygame.display.flip()

                            # player can only reroll once per game so if reroll limit is one then the game will do nothing
                        elif player2_reroll_limit == 1 and round%2 == 0:
                            print("you cannot do this again")

                    #reroll limit for player 1
                        elif player1_reroll_limit == 0:

                            #everytime reroll is activate, the reroll sound will activate
                            pygame.mixer.Sound.play(sound_reroll)

                            #If player initiate reroll then the bullet will randomly place again betwenn 1 and 6
                            bullet = random.randint(1, 6)

                            #reroll limit is once per game
                            player1_reroll_limit += 1

                            #everytime a player take action, the number of round will increase
                            round = round+1

                            screen.blit(bg2, (0, 0))
                            pygame.display.flip()

                        #player can only reroll once per game so if reroll limit is one then the game will do nothing
                        elif player1_reroll_limit == 1:
                            print("you cannot do this again")
