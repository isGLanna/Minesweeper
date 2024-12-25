# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna
# Date: 24/12/2024
# Language: Python 3.11
# -----------------------------------------------

import sys
from AbstractMenu import *
from Settings import *
from DifficultyMenu import *
from RankMenu import *
from ButtonTypes import Buttons
from ButtonTypes import Background


class MainMenu(Menu):
    def __init__(self):
        super().__init__()
        self.width = width
        self.height = height
        self.background = Background(screen1)

        self.button_start = Buttons("Jogar", (200, 60), button1, button2, font_0)
        self.button_rank = Buttons("Rank", (200, 60), button1, button2, font_0)
        self.button_exit = Buttons("Sair", (200, 60), button1, button2, font_0)

        self.button_start.rect.y, self.button_start.rect.x = (height - 60) // 2 - 125, (width - 200) // 2
        self.button_rank.rect.y, self.button_rank.rect.x = (height - 60) // 2, (width - 200) // 2
        self.button_exit.rect.y, self.button_exit.rect.x = (height - 60) // 2 + 125, (width - 200) // 2

        self.buttons = [self.button_start, self.button_rank, self.button_exit]

    def draw_background(self):
        self.background.draw_background()
        self.background.transparent_surface()

    def show(self):
        self.draw_background()
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.quitting()

                if event.type == pygame.MOUSEBUTTONUP:
                    clicked_button = self.get_events()

                    if clicked_button:
                        sound_click.play()

                        if clicked_button == self.button_start:
                            game = DifficultyMenu(self.background)
                            game.show()
                            self.show()

                        elif clicked_button == self.button_rank:
                            game = RankMenu(self.background)
                            game.show()
                            self.show()

                        elif clicked_button == self.button_exit:
                            self.quitting()

            self.button_start.print_display(pygame.mouse.get_pos())
            self.button_rank.print_display(pygame.mouse.get_pos())
            self.button_exit.print_display(pygame.mouse.get_pos())

            pygame.display.update()
            clock.tick(60)

    def get_events(self):
        for button in self.buttons:
            if button.collision_point(pygame.mouse.get_pos()):
                return button
        return None

    def quitting(self):
        pygame.quit()
        sys.exit()
