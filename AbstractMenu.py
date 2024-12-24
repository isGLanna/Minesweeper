import pygame
from abc import ABC, abstractmethod


class Menu(ABC):
    def __init__(self):
        self.buttons = []

    @abstractmethod
    def draw_background(self):
        self.background.draw_background()
        self.background.transparent_surface()

    def buttons(self): pass

    def check_button_collision(self, event):
        for button in self.buttons:
            if button.collision_point(pygame.mouse.get_pos()):
                button.up()
                return button
        return

    def get_events(self):
        for button in self.buttons:
            if event.type == pygame.MOUSEBUTTONUP:
                if button.collision_point(pygame.mouse.get_pos()):
                    return button

    def quitting(self):
        pygame.quit()
        sys.exit()

    def __del__(self): pass