import pygame
class Reroll():
    def __init__(self,screen):
        self.screen=screen
        # loading the image and making the image a rectangle
        self.image=pygame.image.load("reroll.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # the position of the image
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.screen_rect.centerx)
        self.rect.right = self.screen_rect.right

    def blitme(self):
        #Now we want to show the image on the screen
        self.screen.blit(self.image, self.rect)
