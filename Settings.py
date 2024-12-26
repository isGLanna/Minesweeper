# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna
# Date: 23/12/2024
# Language: Python 3.11
# -----------------------------------------------

import pygame
from pygame.locals import *

pygame.init()

# variáveis
mine = 7  # bomba
empty = 0  # campo vazio
unknown = -1  # campo desconhecido
flag = -2  # campo marcado


# cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (196, 213, 230)
LIGHTBLUE = (120, 140, 220)
BLUE = (25, 120, 185)
DARKBLUE = (102, 105, 105)
GREEN = (90, 210, 70)
LIGHTGREEN = (112, 186, 162)
YELLOW = (180, 210, 15)
RED = (160, 25, 20)
DARKRED = (80, 15, 0)
PURPLE = (135, 45, 115)
colors = [None, GREEN, YELLOW, RED, PURPLE, BLACK]

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
font_8 = pygame.font.SysFont('padrão', 26)


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

# imagens
screen1 = "data/image/background_1.jpg"
screen2 = "data/image/background_6.png"

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

# sons
sound_win = pygame.mixer.Sound("data/sound/winning.wav")
sound_lose = pygame.mixer.Sound("data/sound/lose.wav")
sound_click = pygame.mixer.Sound("data/sound/click.wav")

sound_win.set_volume(0.24)
sound_lose.set_volume(0.18)
sound_click.set_volume(0.12)

# tamanhos das telas
size_box_hard = 40, 40
size_box_easy = 50, 50
internal_box = 35, 35
size_button = 270, 75

# textos
text_info = ["___<| Fácil |>___", "12x9", "200 segundos", "___<| Difícil |>___", "16x12", "350 segundo"]
