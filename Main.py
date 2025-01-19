# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna
# Date: 21/04/2024
# Language: Python 3.11
# -----------------------------------------------
import pygame
from GameMachine import GameMachine
from MainMenu import MainMenu
from random import randint

pygame.init()


# >>---------------------------------- FUNÇÃO PRINCIPAL DO MENU ----------------------------------<< #


if __name__ == "__main__":
    game = MainMenu()
    game.show()
