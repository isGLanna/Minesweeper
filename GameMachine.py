from Settings import *
from Display import GenericButtons
from random import randint


# Classe de dados e informações a serem processadas/exibidos ao longo do jogo
class GameMachine:
    lucky = GenericButtons((60, 60), lucky_i[0], True, None)
    lucky.rect.y, lucky.rect.x = 75 - 30, (width // 2 - 42)

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
        self.m = 0
        self.n = 0

        self.first_occurrence = True

        self.list_x_y = []
        self.pos_bombs = []

    def difficulty(self):  # níveis de dificuldade fácil/difícil
        self.m, self.n, self.bombs = (9, 12, 8) if self.level else (12, 16, 18)
        return self.m, self.n, self.bombs

    # Descobre aleatoriamente uma bomba/campo vazio
    def function_lucky(self):
        # revela campo vazio
        def realese_cell():
            var1, var2 = randint(0, self.m - 1), randint(0, self.n - 1)
            if self.matrix_above[var1][var2] == -1:
                self.matrix_above[var1][var2] = empty
                return self.matrix_above
            return realese_cell()

        # revela campo minado
        def realese_mine():
            var1 = randint(0, self.bombs - 1)
            pos = self.get_position_bomb()
            (var2, var3) = pos[var1]
            self.matrix_above[var2][var3] = empty

            self.set_revealed()
            return self.matrix_above

        if self.get_starting():
            print("Partida não criada.\n")
            return self.matrix_above
        if self.lucky.get_lucky() >= 3:
            return print("Acabou sua sorte!")
        else:
            self.lucky.update_lucky()
            luck = randint(0, 1)
            if luck:
                realese_cell()
            else:
                realese_mine()

    # selecionar e imprimir a cor dos números de 'indicação de bomba' de acordo com o array 'colors'
    def draw_number(self):
        if self.starting_game:
            return
        else:
            if self.first_occurrence:
                for i, j in self.position_bomb:
                    for x in range(max(i - 1, 0), min(i + 2, self.m)):
                        for y in range(max(j - 1, 0), min(j + 2, self.n)):
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

    def get_bombs(self): return self.bombs

    def set_limit_flag(self, add): self.number_flag += add

    def get_limit_flag(self): return self.get_bombs() > self.number_flag

    def get_number_flag(self): return self.number_flag

    def get_starting(self): return self.starting_game

    def set_starting(self): self.starting_game = False

    def get_revealed(self): return self.bombs_revealed

    def set_revealed(self): self.bombs_revealed += 1

    def __del__(self): pass
