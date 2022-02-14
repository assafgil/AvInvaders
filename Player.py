import pygame


def get_pressed(key):
    return pygame.key.get_pressed()[key]


class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def display_on_screen(self, display):
        display.blit(self.img, (self.x, self.y))

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def moving(self):

        if self.x < 50:
            self.x = 50

        if self.x > 1850:
            self.x = 1850

        if get_pressed(pygame.K_a):
            self.x -= 6
        if get_pressed(pygame.K_d):
            self.x += 6
