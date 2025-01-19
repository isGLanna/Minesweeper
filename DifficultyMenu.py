# -----------------------------------------------
# Program: Campo Minado
# Date: 24/12/2024
# Language: Python 3.11
# -----------------------------------------------

import sys

import pygame.display
from AbstractMenu import *
from Settings import *
from ButtonTypes import Buttons
from CurrentMatch import *
from Player import Player


class DifficultyMenu(Menu):
    def __init__(self, background):
        super().__init__()
        self.player = Player()
        self.width = width
        self.height = height
        self.size_button = 200, 60
        self.background = background
        self.radius = 12

        self.button_easy = Buttons("Fácil", (200, 60), button1, button2, font_0)
        self.button_hard = Buttons("Difícil", (200, 60), button1, button2, font_0)
        self.button_return = Buttons("Voltar", (180, 55), button1, button2, font_0_return)

        self.button_easy.rect.y, self.button_easy.rect.x = (height - 60) // 2 - 75, (width - 200) // 2
        self.button_hard.rect.y, self.button_hard.rect.x = (height - 60) // 2 + 25, (width - 200) // 2
        self.button_return.rect.y, self.button_return.rect.x = (height - 60) // 2 + 125, (width - 180) // 2

        self.buttons = [self.button_easy, self.button_hard, self.button_return]
        self.action = None

    def draw_background(self):
        self.background.draw_background()
        self.background.transparent_surface()

    def show(self):
        self.draw_background()
        self.button_easy.waiting_for_response(button7, self.size_button)
        self.button_hard.waiting_for_response(button7, self.size_button)

        while not self.action:
            self.action = self.printout_name_insertion()
            if self.action == "*Voltar*":
                return
            clock.tick(FPS)

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.quitting()

                if event.type == pygame.MOUSEBUTTONUP:
                    clicked_button = self.get_events()

                    if clicked_button:
                        sound_click.play()

                        if clicked_button == self.button_easy:
                            return current_match(True, self.player)

                        elif clicked_button == self.button_hard:
                            return current_match(False, self.player)

                        elif clicked_button == self.button_return:
                            return

            self.button_easy.print_display(pygame.mouse.get_pos())
            self.button_hard.print_display(pygame.mouse.get_pos())
            self.button_return.print_display(pygame.mouse.get_pos())
            self.draw_tooltip()

            pygame.display.update()
            clock.tick(60)

    # solicitar nome do jogador para entrada da função 'dificuldade'
    def printout_name_insertion(self):
        corners_radius, enter, input_text, i = 18, False, "", 0

        larg, alt = 152, 120

        # tela para receber nome do jogador
        text = font_6.render('Digite seu nome e ENTER', True, DARKRED)
        display.blit(text, (165, 135))
        pygame.draw.rect(display, RED, (larg, alt, 375, 55), 3, border_radius=corners_radius)
        pygame.display.flip()

        # delay de transição do botão
        while i < 45:
            self.button_return.print_display(pygame.mouse.get_pos())
            self.draw_tooltip()
            pygame.display.update()
            i += 1
            clock.tick(60)

        # bloquear ações enquanto não houver entrada 'Enter' ou 'Voltar'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitting()

                if event.type == MOUSEBUTTONUP:
                    if self.button_return.collision_point(pygame.mouse.get_pos()):
                        return "*Voltar*"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(input_text) != 0:
                            input_text = input_text[:-1]

                    elif event.key == pygame.K_RETURN:
                        enter = True

                    else:
                        if len(input_text) < 16:
                            input_text += event.unicode
                    text = font_5.render(input_text, True, WHITE)

                    self.background.draw_background()
                    self.background.transparent_surface()
                    self.button_easy.waiting_for_response(button7, self.size_button)
                    self.button_hard.waiting_for_response(button7, self.size_button)
                    self.button_return.waiting_for_response(button1, (180, 55))
                    self.button_return.print_display(pygame.mouse.get_pos())
                    self.draw_tooltip()

                    if enter:
                        transparent = pygame.Surface((375, 55), pygame.SRCALPHA)
                        transparent.set_alpha(120)
                        pygame.draw.rect(transparent, LIGHTGREEN, (0, 0, 375, 55), border_radius=corners_radius)
                        display.blit(transparent, (larg, alt))

                    pygame.draw.rect(display, RED, (larg, alt, 375, 55), 3, border_radius=corners_radius)
                    text_rect = text.get_rect(center=(width // 2, 75 * 2))
                    display.blit(text, text_rect)
                    pygame.display.flip()
                    pygame.display.update()

                    if enter:
                        self.player.set_name(input_text)
                        return input_text

            clock.tick(60)

    def draw_tooltip(self):
        circle_x, circle_y = width // 2 + 125, (height - 60) // 2 - 50
        pygame.draw.circle(display, RED, (circle_x, circle_y), self.radius, 2)

        text_i = font_8.render('i', True, DARKRED)
        text_rect = text_i.get_rect(center=(circle_x, circle_y))
        display.blit(text_i, text_rect)

        if pygame.math.Vector2(pygame.mouse.get_pos()).distance_to((circle_x, circle_y)) < self.radius:
            tooltip_surface = pygame.Surface((136, 155), pygame.SRCALPHA)
            tooltip_surface.set_alpha(2)

            pygame.draw.rect(tooltip_surface, RED, (0, 0, 136, 155), border_radius=15)

            line_height = 24
            for i, line in enumerate(text_info):
                text_surface = font_8.render(line, True, WHITE)
                text_rect = text_surface.get_rect(center=(68, 15 + i * line_height))  # Ajuste da posição
                tooltip_surface.blit(text_surface, text_rect)

            display.blit(tooltip_surface, (width // 2 + 145, (height - 60) // 2 - 75))
            pygame.display.update()

    def get_events(self):
        for button in self.buttons:
            if button.collision_point(pygame.mouse.get_pos()):
                return button
        return None

    def quitting(self):
        pygame.quit()
        sys.exit()
