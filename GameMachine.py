# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna
# Date: 23/12/2024
# Language: Python 3.11'
# -----------------------------------------------

from Settings import *
from ButtonTypes import GenericButtons
from random import randint


# Classe de dados e informações a serem processadas/exibidos ao longo do jogo
class GameMachine:
    lucky = GenericButtons((60, 60), lucky_i[0], True, None)
    lucky.rect.y, lucky.rect.x = 75 - 30, (width // 2 - 42)

    def __init__(self, level, player):
        self.mine_image = pygame.image.load(mine_i).convert_alpha()
        self.mine_image = pygame.transform.scale(self.mine_image, (46, 46))
        self.starting_game = True
        self.matrix_below = [[]]
        self.matrix_above = [[]]
        self.player = player

        self.number_flag = 0
        self.position_bomb = []
        self.bombs_revealed = 0
        self.bombs = 0
        self.level = level
        self.h = 0
        self.w = 0

        self.first_occurrence = True

        self.list_x_y = []
        self.pos_bombs = []

    def difficulty(self):  # níveis de dificuldade fácil/difícil
        self.h, self.w, self.bombs = (9, 12, 8) if self.level else (12, 16, 18)     # h , w = height, width
        return self.w, self.h, self.bombs
        # lógica está invertida entre altura e largura, mas vai ficar assim

    def create_matrix(self, pos_x, pos_y):
        w, h = self.h, self.w
        empty_matrix = [[0] * w for _ in range(h)]
        bomb_insert = 0
        pos_x_y = []
        list_x_y = [(pos_x - 1, pos_y - 1), (pos_x, pos_y - 1), (pos_x + 1, pos_y - 1),
                    (pos_x - 1, pos_y), (pos_x, pos_y), (pos_x + 1, pos_y),
                    (pos_x - 1, pos_y + 1), (pos_x, pos_y + 1), (pos_x + 1, pos_y + 1)]

        while self.bombs > bomb_insert:
            i, j = randint(0, h - 1), randint(0, w - 1)

            if not empty_matrix[i][j] == mine and (i, j) not in list_x_y:
                empty_matrix[i][j] = mine
                pos_x_y.append((i, j))
                bomb_insert += 1

        self.position_bomb = pos_x_y

        for x, y in pos_x_y:
            for i in range(max(0, x - 1), min(x + 2, h)):
                for j in range(max(0, y - 1), min(y + 2, w)):
                    if empty_matrix[i][j] != mine:
                        empty_matrix[i][j] += 1

        for j in range(w):
            column = [empty_matrix[i][j] for i in range(h)]
            print(f" {j + 1}: {column}")

        self.set_matrix(empty_matrix)

    def limit_time(self, count):  # imprime contagem regressiva
        if self.level:
            tempo = 200
        else:
            tempo = 350

        if count == 999 * delay:
            count = tempo * 15

        i = tempo - count // 15
        pygame.draw.rect(display, GREY, (535, 62, 76, 40))
        str1, str2 = 'TIME', str(i)
        text1 = font_1.render(str1, True, BLUE)
        text2 = font_1.render(str2, True, RED)
        display.blit(text1, (450, 60))
        display.blit(text2, (545, 60))
        pygame.display.update()

        if self.get_starting():
            return count

        if i <= 0:
            print('O tempo esgotou')
            self.declare_defeat()

        self.player.set_time(tempo - i)
        count += 1
        return count

    def declare_defeat(self):
        self.make_sound(sound_lose)

        pos = self.get_position_bomb()
        matrix = self.get_matrix_above()
        for i, j in pos:
            matrix[i][j] = empty
        self.draw_number()

        self.transparent_surface()
        text = font_2.render('DERROTA', True, RED)
        text_rect = text.get_rect()
        text_rect.midtop = (width // 2, height // 2 - 25)
        display.blit(text, text_rect)
        pygame.display.flip()

        self.lucky.restart_lucky()
        return self.time_to_exit()

    def declare_win(self, last_render):
        matrix, bombs, bombs_revealed = self.get_matrix_above(), self.get_bombs(), self.get_revealed()
        partial_result = bombs - bombs_revealed

        count_cells = sum(row.count(unknown) for row in matrix)
        count_cells += sum(row.count(flag) for row in matrix)
        if count_cells > partial_result:
            return

        pos = self.get_position_bomb()
        for i, j in pos:
            matrix[i][j] = empty
        self.set_matrix_above(matrix)

        if not last_render:
            return True

        self.player.save_data_player()

        self.make_sound(sound_win)

        # exibir vitória
        self.transparent_surface()
        text = font_2.render('VITORIA', True, GREEN)
        text_rect = text.get_rect()
        text_rect.midtop = (width // 2, height // 2 - 25)
        display.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(1)
        self.lucky.restart_lucky()
        return self.time_to_exit()

    def discover(self, x, y):
        h, w = self.w, self.h

        # Se a célula já foi clicada ou é uma bomb, não vai fazer nada
        if self.matrix_above[x][y] != unknown or self.matrix_below[x][y] == mine:
            return

        # mostra a célula
        self.matrix_above[x][y] = empty

        # Se a célula aos lados nao tem bomba, mostra células ao redor recursivamente!
        if self.matrix_below[x][y] == empty:
            for i in range(max(0, x - 1), min(x + 2, h)):
                for j in range(max(0, y - 1), min(y + 2, w)):
                    if self.matrix_above[i][j] == unknown:
                        self.discover(i, j)

        return self.matrix_above

    # Descobre aleatoriamente uma bomba/campo vazio
    def function_lucky(self):
        # revela campo vazio
        def realese_cell():
            var1, var2 = randint(0, self.w - 1), randint(0, self.h - 1)
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
            return self.matrix_above
        if self.lucky.get_lucky() >= 3:
            return print("Acabou sua sorte!")
        else:
            self.lucky.update_lucky()
            luck = randint(0, 2)    # 66% chance descobrir bomba, 33% campo vazio
            if luck:
                realese_cell()
            else:
                realese_mine()

    # Função para exibir o efeito de transparência (mesma do código original)
    def transparent_surface(self):
        corners_radius = 25
        transparent = pygame.Surface((width, height), pygame.SRCALPHA)
        transparent.set_alpha(200)
        pygame.draw.rect(transparent, DARKBLUE, (0, 0, 230, 70), border_radius=corners_radius)
        display.blit(transparent, (width // 2 - 115, 280))
        pygame.display.update()

    def time_to_exit(self):
        timer = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                    return "Restart"

            timer += 1
            if timer == 90 * 10:
                return "Restart"
            clock.tick(90)

    # selecionar e imprimir a cor dos números de 'indicação de bomba' de acordo com o array 'colors'
    def draw_number(self):
        matrix_above = self.get_matrix_above()  # Usar uma variável local para referência
        matrix_below = self.get_matrix()  # Também pode ser aplicado para matrix_below

        if self.starting_game:
            return
        else:
            if self.first_occurrence:

                self.list_x_y.extend(
                    (x, y)
                    for i, j in self.position_bomb
                    for x in range(max(i - 1, 0), min(i + 2, self.w))
                    for y in range(max(j - 1, 0), min(j + 2, self.h))
                )

                self.first_occurrence = False

            for x, y in self.list_x_y:  # Desenhar no contorno da bomba
                if matrix_above[x][y] == 0:  # Usando matrix_above local
                    if matrix_below[x][y] != mine:
                        text = number_font.render(
                            str(matrix_below[x][y]), True, colors[matrix_below[x][y]]
                        )

                        if self.level:
                            display.blit(text, ((x * 50) + 40 + 15, ((y * 50) + 130 + 5)))
                        else:
                            display.blit(text, ((x * 40) + 20 + 10, (y * 40) + 120 + 2))
                    else:
                        if self.level:
                            display.blit(self.mine_image, ((x * 50) + 40, (y * 50) + 130))
                        else:
                            display.blit(self.mine_image, ((x * 40) + 20 - 4, (y * 40) + 120 - 6))


    def make_sound(self, audio):
        audio.play()

    def set_matrix_above(self, matrix_above): self.matrix_above = matrix_above

    def get_matrix_above(self): return self.matrix_above

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
