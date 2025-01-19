# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna
# Date: 24/12/2024
# Language: Python 3.11
# -----------------------------------------------

import pygame
from abc import ABC, abstractmethod


class Menu(ABC):
    def __init__(self):
        self.buttons = []

    @abstractmethod
    def draw_background(self): pass

    @abstractmethod
    def get_events(self): pass

    @abstractmethod
    def quitting(self): pass
