import pygame


class Av:
    def __init__(self, x, y, animation_array):
        self.x = x
        self.y = y
        self.frame = 0
        self.step = 9
        self.animation_array = animation_array
        self.change_move = False

    def moving(self):
        if not self.change_move:
            self.x += self.step

        if self.x > 1500:
            self.y += 50
            self.change_move = True

        if self.change_move:
            self.x -= self.step

        if self.x < 100:
            self.change_move = False

    def display_on_screen(self, display):
        display.blit(self.animation_array[self.frame], (self.x, self.y))

    def change_animation(self):
        if self.frame != 3:
            self.frame += 1
        else:
            self.frame = 0

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.animation_array[self.frame].get_width(),
                           self.animation_array[self.frame].get_height())
