# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna e Elisa Ribeiro
# Date: 21/12/2024
# Language: Python 3.11
# -----------------------------------------------
import pygame
from GameMachine import GameMachine
from MainMenu import MainMenu
from random import randint

pygame.init()

if __name__ == "__main__":
    game = MainMenu()
    game.show()
