# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna
# Date: 25/12/2024
# Language: Python 3.11
# -----------------------------------------------

import sys
from AbstractMenu import *
from Settings import *
from ButtonTypes import Buttons
from ButtonTypes import Background
from Rank import fetch_players


class RankMenu(Menu):
    def __init__(self, background):
        super().__init__()
        self.level = 1
        self.width = width
        self.height = height
        self.background = background

        self.button_return = Buttons("Voltar", (100, 40), button5, button6, font_4)
        self.button_easy = Buttons("Fácil", (115, 48), button3, button4, font_3)
        self.button_hard = Buttons("Difícil", (115, 48), button5, button6, font_3)

        self.button_return.rect.y, self.button_return.rect.x = 10, 0
        self.button_easy.rect.y, self.button_easy.rect.x = 54, width // 2 - 115 - 2
        self.button_hard.rect.y, self.button_hard.rect.x = 54, width // 2 + 2

        self.buttons = [self.button_return, self.button_easy, self.button_hard]

    def draw_background(self):
        self.background.draw_background()
        self.printout_rank()

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

                        if clicked_button == self.button_return:
                            return

                        elif clicked_button == self.button_easy:
                            self.set_level()
                            self.draw_background()

                        elif clicked_button == self.button_hard:
                            self.set_level()
                            self.draw_background()

            self.button_return.print_display(pygame.mouse.get_pos())
            self.button_easy.print_display(pygame.mouse.get_pos())
            self.button_hard.print_display(pygame.mouse.get_pos())

            pygame.display.update()
            clock.tick(60)

    def printout_rank(self):
        corners_radius = 25
        players_easy_mod, players_hard_mod = fetch_players()

        transparent = pygame.Surface((width, height), pygame.SRCALPHA)
        transparent.set_alpha(135)

        pygame.draw.rect(transparent, DARKBLUE, (0, 0, width * 0.7, height * 0.75), border_radius=corners_radius)
        display.blit(transparent, (102, 110))

        pygame.draw.line(display, GREY, (width // 2 - 1, 54), (width // 2 - 1, 101), 5)
        pygame.draw.line(display, GREY, (395, 115), (395, 560), 3)

        pygame.draw.line(display, GREY, (105, 145), (380, 145), 2)
        pygame.draw.line(display, GREY, (410, 145), (560, 145), 2)

        text_1, text_2 = font_6.render("Nome", True, WHITE), font_6.render("Tempo", True, WHITE)

        display.blit(text_1, (210, 118)), display.blit(text_2, (440, 118))

        i = 1
        if self.level:
            search = players_easy_mod
        else:
            search = players_hard_mod
        for player in search:
            name, time = player
            text_3, text_4 = font_6.render(f"{i}º   " + name, True, GREY), font_6.render(str(time), True, GREY)
            display.blit(text_3, (117, 120 + 40 * i))
            display.blit(text_4, (470, 120 + 40 * i))
            i += 1
            if i > 10:
                break

    def set_level(self):
        self.level = abs(self.level - 1)
        self.printout_rank()

    def get_events(self):
        for button in self.buttons:
            if button.collision_point(pygame.mouse.get_pos()):
                return button
        return None

    def quitting(self):
        pygame.quit()
        sys.exit()
