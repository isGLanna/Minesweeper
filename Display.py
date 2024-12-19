# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna e Elisa Ribeiro
# Date: 18/07/2024
# Language: Python 3.11
# -----------------------------------------------

import pygame
import sys
from pygame.locals import *
from Rank import *


pygame.init()

# variáveis
mine = 7                # campo minado
flag = -2               # campo marcado
size_button = 270, 75

# cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (196, 213, 230)
LIGHTBLUE = (120, 140, 220)
BLUE = (25, 120, 185)
DARKBLUE = (102, 105, 105)
GREEN = (90, 210, 70)
YELLOW = (180, 210, 15)
RED = (160, 25, 20)
DARKRED = (80, 15, 0)
PURPLE = (135, 45, 115)

# imagens
screen1 = "data/image/background_1.jpg"
screen2 = "data/image/background_6.png"

# fonte
number_font = pygame.font.SysFont('padrão', 54)
font_0 = pygame.font.SysFont('padrão', 62)
font_0_return = pygame.font.SysFont('padrão', 50)
font_1 = pygame.font.Font("data/font/DS-DIGIB.TTF", 42)
font_2 = pygame.font.Font("data/font/DS-DIGIB.TTF", 56)
font_3 = pygame.font.SysFont('padrão', 38)
font_4 = pygame.font.SysFont('padrão', 46)
font_5 = pygame.font.SysFont('padrão', 52)
font_6 = pygame.font.SysFont('padrão', 42)
font_7 = pygame.font.SysFont('padrão', 44)

# screen settings
height = 620
width = 680
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 45
delay = 15

logo = pygame.image.load("data/image/image_game.png")
pygame.display.set_caption('Py Of All Bombs')
pygame.display.set_icon(logo)

# Carregue as imagens com transparência
button1 = pygame.image.load('data/image/button_blue1.png').convert_alpha()
button2 = pygame.image.load('data/image/button_blue2.png').convert_alpha()
button3 = pygame.image.load('data/image/left_half_button_blue1.png').convert_alpha()
button4 = pygame.image.load('data/image/left_half_button_blue2.png').convert_alpha()
button5 = pygame.image.load('data/image/right_half_button_blue1.png').convert_alpha()
button6 = pygame.image.load('data/image/right_half_button_blue2.png').convert_alpha()
button7 = pygame.image.load('data/image/button_blue3.png').convert_alpha()

#   transparência das imagens dos botões
button1.set_alpha(75)
button2.set_alpha(75)
button3.set_alpha(75)
button4.set_alpha(75)
button5.set_alpha(75)
button6.set_alpha(75)
button7.set_alpha(75)

box1 = "data/image/button_box.png"
flag_i = "data/image/box_with_flag.png"
mine_i = "data/image/mine.png"
flag_image = "data/image/flag_1.png"
lucky_i = ["data/image/lucky_1.png", "data/image/lucky_2.png",
           "data/image/lucky_3.png", "data/image/lucky_4.png"]

# cor dos números
colors = [None, GREEN, YELLOW, RED, PURPLE, BLACK]


class Background:
    def __init__(self, called_image):
        self.corners_radius = 25
        self.transparent = pygame.Surface((width, height), pygame.SRCALPHA)
        self.transparent.set_alpha(95)
        self.image = pygame.image.load(called_image).convert()

        self.image = pygame.transform.smoothscale(self.image, (width, height))

    def transparent_surface(self):
        pygame.draw.rect(self.transparent, DARKBLUE, (0, 0, 400, 420), border_radius=self.corners_radius)
        display.blit(self.transparent, (width//2 - 200, 105))
        pygame.display.update()

    def draw_background(self):
        display.blit(self.image, (0, 0))

    def __del__(self): pass


# botões interativos com transições entre imagens
class Buttons:
    def __init__(self, text, size, image_0, image_1, fonte):
        self.background = Background(screen1)
        self.text = text
        self.alpha = 0

        self.image_up = image_0
        self.image_down = image_1

        self.image_up = pygame.transform.scale(self.image_up, size)
        self.image_down = pygame.transform.scale(self.image_down, size)

        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect = self.image_down.get_rect()

        self.click = False
        self.text_surface = None
        self.text_rect = None

        self.font = fonte

        self.render_text()

    # renderizar imagem com texto
    def render_text(self):
        # definir níveis de opacidade (não faço ideia de como funciona)
        self.image_up.set_alpha(18)
        self.image_down.set_alpha(18)

        self.text_surface = self.font.render(self.text, True, WHITE)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.image_up.blit(self.text_surface, self.text_rect)
        self.image_down.blit(self.text_surface, self.text_rect)
        clock.tick(FPS)

    # atualizar botão de acordo com ponteiro
    def print_display(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            display.blit(self.image_down if not self.click else self.image_up, self.rect)
        else:
            display.blit(self.image_up if not self.click else self.image_down, self.rect)

    # aguarda algum retorno do usuário para continuar
    def waiting_for_response(self, image_file, size):
        image = image_file
        image = pygame.transform.scale(image, size)

        self.text_surface = self.font.render(self.text, True, WHITE)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

        display.blit(image, self.rect)
        display.blit(self.text_surface, self.text_rect)

    # retornar condição de colisão: True/False
    def collision_point(self, pos): return self.rect.collidepoint(pos)

    def down(self): self.click = True

    def up(self): self.click = False

    def __del__(self): pass


class GameBox:
    def __init__(self, size_per_level):

        self.box = pygame.image.load(box1).convert()
        self.flag = pygame.image.load(flag_i).convert_alpha()

        self.box = pygame.transform.scale(self.box, size_per_level)
        self.flag = pygame.transform.scale(self.flag, size_per_level)

        self.image = self.box
        self.rect = self.image.get_rect()

        self.surface = None

    def draw_game(self, flag_no_flag):
        display.blit(self.box, self.rect)
        if flag_no_flag == flag:
            display.blit(self.flag, self.rect)

    def collision_point(self, mouse_pos): return self.rect.collidepoint(mouse_pos)

    def __del__(self): pass


class GenericButtons:
    def __init__(self, size, called_image, collision, text=''):
        self.size = size
        self.collision = collision
        self.text = text
        self.text_surface = None
        self.position = []

        self.image = pygame.image.load(called_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

        self.lucky = 0

    def draw_button(self):
        if self.text:
            self.text_surface = number_font.render(str(self.text), True, BLACK)
            display.blit(self.text_surface, (self.rect.x + 50, self.rect.y + 8))

        display.blit(self.image, self.rect)

    def collision_point(self, pos): return self.rect.collidepoint(pos)

    def update_flag(self, add):
        int(self.text)
        self.text -= add
        self.draw_button()

    # atualiza imagem após interação
    def update_lucky(self):
        self.lucky += 1
        self.image = pygame.image.load(lucky_i[self.lucky]).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

    def get_lucky(self):
        return self.lucky

    def __del__(self): pass


# Classe de dados e informações a serem processadas/exibidos ao longo do jogo
class StartGame:
    def __init__(self, level):
        self.mine_image = pygame.image.load(mine_i).convert_alpha()
        self.mine_image = pygame.transform.scale(self.mine_image, (46, 46))
        self.starting_game = True
        self.matrix_below = None
        self.matrix_above = None

        self.number_flag = 0
        self.position_bomb = []
        self.bombs_revealed = 0
        self.bombs = 0
        self.level = level

        self.first_occurrence = True

        self.list_x_y = []
        self.pos_bombs = []

    # selecionar e imprimir a cor dos números de 'indicação de bomba' de acordo com o array 'colors'
    def draw_number(self):
        if self.starting_game:
            return
        else:
            if self.first_occurrence:
                if self.level:
                    n, m = 9, 12
                else:
                    n, m = 12, 16
                for i, j in self.position_bomb:
                    for x in range(max(i - 1, 0), min(i + 2, m)):
                        for y in range(max(j - 1, 0), min(j + 2, n)):
                            self.list_x_y.append((x, y))
                self.first_occurrence = False

            for x, y in self.list_x_y:               # desenhar no contorno da bomba
                if self.matrix_above[x][y] == 0:
                    if self.matrix_below[x][y] != mine:
                        text = number_font.render(str(self.matrix_below[x][y]), True, colors[self.matrix_below[x][y]])
                        if self.level:
                            display.blit(text, ((x * 50) + 40 + 15, ((y * 50) + 130 + 5)))
                        else:
                            display.blit(text, ((x * 40) + 20 + 10, (y * 40) + 120 + 2))
                    else:
                        if self.level:
                            display.blit(self.mine_image, ((x * 50) + 40, (y * 50) + 130))
                        else:
                            display.blit(self.mine_image, ((x * 40) + 20 - 4, (y * 40) + 120 - 6))

    def set_matrix_above(self, matrix_above): self.matrix_above = matrix_above

    def get_matrix_above(self): return self.matrix_above

    def set_position_bomb(self, position_bomb): self.position_bomb = position_bomb

    def get_position_bomb(self): return self.position_bomb

    def get_matrix(self): return self.matrix_below

    def set_matrix(self, matrix): self.matrix_below = matrix

    def set_bombs(self, bombs): self.bombs = bombs

    def get_bombs(self): return self.bombs

    def set_limit_flag(self, add): self.number_flag += add

    def get_limit_flag(self): return self.get_bombs() > self.number_flag

    def get_number_flag(self): return self.number_flag

    def get_starting(self): return self.starting_game

    def set_starting(self): self.starting_game = False

    def get_revealed(self): return self.bombs_revealed

    def set_revealed(self): self.bombs_revealed += 1

    def __del__(self): pass


class Player:
    name = None
    time = 0
    level = 0

    def save_data_player(self):
        insert_player(self.name, self.time, self.level)

    def __del__(self): pass


def printout_rank(level):
    corners_radius = 20
    players_easy_mod, players_hard_mod = fetch_players()

    transparent = pygame.Surface((width, height), pygame.SRCALPHA)
    transparent.set_alpha(135)
    pygame.draw.rect(transparent, DARKBLUE, (0, 0, width * 0.7, height * 0.75), border_radius=corners_radius)
    display.blit(transparent, (102, 110))

    pygame.draw.line(display, GREY, (width//2 - 1, 54), (width//2 - 1, 101), 5)
    pygame.draw.line(display, GREY, (395, 115), (395, 560), 3)

    pygame.draw.line(display, GREY, (105, 145), (380, 145), 2)
    pygame.draw.line(display, GREY, (410, 145), (560, 145), 2)

    text_1 = font_6.render("Nome", True, WHITE)
    text_2 = font_6.render("Tempo", True, WHITE)

    display.blit(text_1, (210, 118))
    display.blit(text_2, (440, 118))

    i = 1
    if level:
        search = players_easy_mod
    else:
        search = players_hard_mod
    for player in search:
        info_1, info_2 = player
        text_3, text_4 = font_6.render(f"{i}º   " + info_1, True, GREY), font_6.render(str(info_2), True, GREY)
        display.blit(text_3, (117, 120 + 40 * i))
        display.blit(text_4, (470, 120 + 40 * i))
        i += 1
        if i > 10:
            break


# solicitar nome do jogador para entrada da função 'dificuldade'
def printout_name_insertion(easy, hard, button_return):
    corners_radius, enter, input_text, i = 18, False, "", 0

    larg, alt = 152, 145

    # tela para receber nome do jogador
    text = font_6.render('Digite seu nome e ENTER', True, DARKRED)
    display.blit(text, (165, 160))
    pygame.draw.rect(display, RED, (larg, alt, 375, 55), 3, border_radius=corners_radius)
    pygame.display.flip()

    # delay de transição do botão
    while i < 45:
        button_return.print_display(pygame.mouse.get_pos())
        pygame.display.update()
        i += 1
        clock.tick(70)

    # bloquear ações enquanto não houver entrada 'Enter' ou 'Voltar'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONUP:
                if button_return.collision_point(pygame.mouse.get_pos()):
                    return "Voltar"
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

                background.draw_background()
                background.transparent_surface()
                easy.waiting_for_response(button7, size_button)
                hard.waiting_for_response(button7, size_button)
                button_return.waiting_for_response(button1, (180, 55))
                button_return.print_display(pygame.mouse.get_pos())

                if enter:
                    transparent = pygame.Surface((375, 55), pygame.SRCALPHA)
                    transparent.set_alpha(80)
                    pygame.draw.rect(transparent, GREEN, (0, 0, 375, 55), border_radius=corners_radius)
                    display.blit(transparent, (larg, alt))

                pygame.draw.rect(display, RED, (larg, alt, 375, 55), 3, border_radius=corners_radius)
                text_rect = text.get_rect(center=(width//2, 87 * 2))
                display.blit(text, text_rect)
                pygame.display.flip()
                pygame.display.update()

                if enter:
                    return input_text

        clock.tick(120)


background = Background(screen1)
