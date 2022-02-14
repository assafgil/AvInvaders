import pygame


class Shot:
    def __init__(self, x, y, img, step):
        self.x = x
        self.y = y
        self.img = img
        self.step = step

    def moving(self):
        self.y -= self.step

    def moving_down(self):
        self.y += self.step

    def display_on_screen(self, display):
        display.blit(self.img, (self.x, self.y))

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
