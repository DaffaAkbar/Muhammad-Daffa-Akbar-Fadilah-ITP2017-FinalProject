import pygame
class Shoot_Button():
    def __init__(self,screen):
        self.screen=screen
        #loading the image and making the image a rectangle
        self.image=pygame.image.load("shoot.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #the position of the image
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.center

    def blitme(self):
        #Now we want to show the image on the screen
        self.screen.blit(self.image, self.rect)

