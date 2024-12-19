# -----------------------------------------------
# Program: Campo Minado
# Developers: Giordano Lanna e Elisa Ribeiro
# Date: 21/07/2024
# Language: Python 3.11
# -----------------------------------------------

from random import randint
from Display import *

pygame.init()

# variáveis
mine = 7  # bomba
empty = 0  # campo vazio
unknown = -1  # campo desconhecido
flag = -2  # campo marcado

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


def make_sound(audio):
    audio.play()


def difficulty_menu():
    text1, text2, text3 = "Fácil", "Difícil", "Voltar"

    button_easy = Buttons(text1, size_button, button1, button2, font_0)
    button_hard = Buttons(text2, size_button, button1, button2, font_0)
    button_return = Buttons(text3, (180, 55), button1, button2, font_0_return)

    button_easy.rect.y, button_easy.rect.x = (height - size_button[1]) // 2 - 20, (width - size_button[0]) // 2
    button_hard.rect.y, button_hard.rect.x = (height - size_button[1]) // 2 + 100, (width - size_button[0]) // 2
    button_return.rect.y, button_return.rect.x = (height - size_button[1]) // 2 - 245, (
            width - size_button[0]) // 2 - 190

    background.draw_background()
    background.transparent_surface()
    button_easy.waiting_for_response(button7, size_button)
    button_hard.waiting_for_response(button7, size_button)

    action = False
    while not action:
        action = printout_name_insertion(button_easy, button_hard, button_return)
        clock.tick(FPS)

    if action == "Voltar":
        return "Voltar"

    player.name = action

    while True:
        button_easy.print_display(pygame.mouse.get_pos())
        button_hard.print_display(pygame.mouse.get_pos())
        button_return.print_display(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if button_easy.collision_point(pygame.mouse.get_pos()):
                    button_easy.up()
                    make_sound(sound_click)
                    player.level = 1
                    return True
                elif button_hard.collision_point(pygame.mouse.get_pos()):
                    button_hard.up()
                    make_sound(sound_click)
                    player.level = 0
                    return False
                elif button_return.collision_point(pygame.mouse.get_pos()):
                    button_return.up()
                    return "Voltar"
        clock.tick(FPS)
        pygame.display.update()


# Função de rank
def display_rank():
    size = 150, 45
    button_return = Buttons("Voltar", size, button5, button6, font_4)
    button_easy = Buttons("Fácil", (115, 48), button3, button4, font_3)
    button_hard = Buttons("Difícil", (115, 48), button5, button6, font_3)

    button_return.rect.y, button_return.rect.x = 10, -15
    button_easy.rect.y, button_easy.rect.x = 54, width // 2 - 115 - 2
    button_hard.rect.y, button_hard.rect.x = 54, width // 2 + 2

    background.draw_background()

    printout_rank(1)

    while True:
        button_return.print_display(pygame.mouse.get_pos())
        button_easy.print_display(pygame.mouse.get_pos())
        button_hard.print_display(pygame.mouse.get_pos())

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if button_easy.collision_point(pygame.mouse.get_pos()):
                    background.draw_background()
                    make_sound(sound_click)
                    printout_rank(1)
            if event.type == MOUSEBUTTONDOWN:
                if button_hard.collision_point(pygame.mouse.get_pos()):
                    background.draw_background()
                    make_sound(sound_click)
                    printout_rank(0)
            if event.type == MOUSEBUTTONDOWN:
                if button_return.collision_point(pygame.mouse.get_pos()):
                    return "Voltar"
        clock.tick(FPS)


def quit_game():
    pygame.quit()
    sys.exit()


# Função de menu principal
def main_menu():
    button_start = Buttons("Jogar", size_button, button1, button2, font_0)
    button_rank = Buttons("Rank", size_button, button1, button2, font_0)
    button_exit = Buttons("Sair", size_button, button1, button2, font_0)

    button_start.rect.y, button_start.rect.x = (height - size_button[1]) // 2 - 125, (width - size_button[0]) // 2
    button_rank.rect.y, button_rank.rect.x = (height - size_button[1]) // 2, (width - size_button[0]) // 2
    button_exit.rect.y, button_exit.rect.x = (height - size_button[1]) // 2 + 125, (width - size_button[0]) // 2

    background.draw_background()
    background.transparent_surface()
    while True:

        button_start.print_display(pygame.mouse.get_pos())
        button_rank.print_display(pygame.mouse.get_pos())
        button_exit.print_display(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()

            if event.type == MOUSEBUTTONUP:
                if button_start.collision_point(pygame.mouse.get_pos()):
                    button_start.up()
                    return "Jogar"
                elif button_rank.collision_point(pygame.mouse.get_pos()):
                    button_rank.up()
                    return "Rank"
                elif button_exit.collision_point(pygame.mouse.get_pos()):
                    button_exit.up()
                    return "Sair"
        clock.tick(90)
        pygame.display.update()


def current_match(level):  # Função interna do jogo campo minado

    match = StartGame(level)

    while True:

        def difficulty():  # níveis de dificuldade fácil/difícil
            if level:
                j, i, n_bomb = 9, 12, 12
            else:
                j, i, n_bomb = 12, 16, 21
            match.set_bombs(n_bomb)
            return i, j, n_bomb

        def create_matrix(pos_x, pos_y):
            empty_matrix = [[0] * n for _ in range(m)]
            bomb_insert = 0
            pos_x_y = []
            list_x_y = [(pos_x - 1, pos_y - 1), (pos_x, pos_y - 1), (pos_x + 1, pos_y - 1),
                        (pos_x - 1, pos_y), (pos_x, pos_y), (pos_x + 1, pos_y),
                        (pos_x - 1, pos_y + 1), (pos_x, pos_y + 1), (pos_x + 1, pos_y + 1)]

            while bomb > bomb_insert:
                i, j = randint(0, m - 1), randint(0, n - 1)

                if not empty_matrix[i][j] == mine and (i, j) not in list_x_y:
                    empty_matrix[i][j] = mine
                    pos_x_y.append((i, j))
                    bomb_insert += 1

            match.set_position_bomb(pos_x_y)

            for x, y in pos_x_y:
                for i in range(max(0, x - 1), min(x + 2, m)):
                    for j in range(max(0, y - 1), min(y + 2, n)):
                        if empty_matrix[i][j] != mine:
                            empty_matrix[i][j] += 1

            for j in range(n):
                column = [empty_matrix[i][j] for i in range(m)]
                print(f" {j + 1}: {column}")

            return empty_matrix

        def limit_time(count):  # imprime contagem regressiva
            if level:
                tempo = 180
            else:
                tempo = 300

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

            if match.get_starting():
                return count

            if i <= 0:
                print('O tempo esgotou')
                declare_defeat()

            player.time = tempo - i
            count += 1
            return count

        def time_to_exit():
            timer = 0
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit_game()
                    if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                        return main_game_loop()

                timer += 1
                if timer == 90 * 10:
                    return main_game_loop()
                clock.tick(90)

        def transparent_surface():
            corners_radius = 25
            transparent = pygame.Surface((width, height), pygame.SRCALPHA)
            transparent.set_alpha(200)
            pygame.draw.rect(transparent, DARKBLUE, (0, 0, 230, 70), border_radius=corners_radius)
            display.blit(transparent, (width // 2 - 115, 280))
            pygame.display.update()

        def declare_defeat():  # chamar retornos para derrota
            make_sound(sound_lose)

            pos = match.get_position_bomb()
            matrix = match.get_matrix_above()
            for i, j in pos:
                matrix[i][j] = empty
            match.draw_number()

            transparent_surface()
            text = font_2.render('DERROTA', True, RED)
            text_rect = text.get_rect()
            text_rect.midtop = (width // 2, height // 2 - 25)
            display.blit(text, text_rect)
            pygame.display.flip()

            time_to_exit()

        def declare_win(last_render):
            matrix, bombs, bombs_revealed = match.get_matrix_above(), match.get_bombs(), match.get_revealed()
            partial_result = bombs - bombs_revealed

            count_cells = sum(row.count(unknown) for row in matrix)
            count_cells += sum(row.count(flag) for row in matrix)
            if count_cells > partial_result:
                return

            pos = match.get_position_bomb()
            for i, j in pos:
                matrix[i][j] = empty
            match.set_matrix_above(matrix)

            if not last_render:
                return True

            player.save_data_player()

            make_sound(sound_win)

            # exibir vitória
            transparent_surface()
            text = font_2.render('VIT0RIA', True, GREEN)
            text_rect = text.get_rect()
            text_rect.midtop = (width // 2, height // 2 - 25)
            display.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(1)
            time_to_exit()

        # recebe campo minado, variável da posição
        '''def discover(matrix_above, x, y):
            matrix_below = match.get_matrix()

            if matrix_above[x][y] == empty or matrix_below[x][y] == mine:
                return

            # caso haja bomba no contorno retornar
            for i in range(max(0, x - 1), min(x + 2, m)):
                for j in range(max(0, y - 1), min(y + 2, n)):
                    if matrix_below[i][j] == mine:
                        return matrix_above

            for i in (-1, 2): # nao tem como, o i vai ser -1 e 2?
                for j in range(-1, 2):
                    for a in range(max(0, x - 1), min(x + 2, m)):
                        for b in range(max(0, y - 1), min(y + 2, n)):
                            matrix_above[a][b] = empty
                    nx, ny = x + i, y + j
                    if 0 <= ny < len(matrix_above[0]) and 0 <= nx < len(matrix_above):
                        discover(matrix_above, nx, ny)
            return matrix_above'''

        def discover(matrix_above, x, y):
            matrix_below = match.get_matrix()
            m = len(matrix_above)
            n = len(matrix_above[0])

            # Se a célula já foi clicada ou é uma bomb, não vai fazer nada
            if matrix_above[x][y] != unknown or matrix_below[x][y] == mine:
                return

            # mostra a célula
            matrix_above[x][y] = empty

            # Se a célula aos lados nao tem bomba, mostra células ao redor RECURSIVAMENTE!!
            if matrix_below[x][y] == empty:
                for i in range(max(0, x - 1), min(x + 2, m)):
                    for j in range(max(0, y - 1), min(y + 2, n)):
                        if matrix_above[i][j] == unknown:
                            discover(matrix_above, i, j)

            return matrix_above

        # Descobre aleatoriamente uma bomba/campo vazio
        def function_lucky(matrix_above):

            # revela campo vazio
            def realese_cell():
                var1, var2 = randint(0, m - 1), randint(0, n - 1)
                if matrix_above[var1][var2] == -1:
                    matrix_above[var1][var2] = empty
                    return matrix_above
                return realese_cell()

            # revela campo minado
            def realese_mine():
                var1 = randint(0, bomb - 1)
                pos = match.get_position_bomb()
                (var2, var3) = pos[var1]
                matrix_above[var2][var3] = empty

                match.set_revealed()
                return matrix_above

            if match.get_starting():
                print("Partida não criada.\n")
                return matrix_above
            if lucky.get_lucky() >= 3:
                return print("Acabou sua sorte!")
            else:
                lucky.update_lucky()
                print(lucky.get_lucky())
                luck = randint(0, 1)
                if luck:
                    realese_cell()
                else:
                    realese_mine()

        # >>---------------------------------- FUNÇÃO INTERNA DE JOGO ----------------------------------<< #

        # Geração do campo minado
        m, n, bomb = difficulty()

        flag_limit = GenericButtons((35, 35), flag_image, False, (match.get_bombs() - match.get_number_flag()))
        flag_limit.rect.x, flag_limit.rect.y = 70, 60

        lucky = GenericButtons((60, 60), lucky_i[0], True, None)
        lucky.rect.y, lucky.rect.x = 75 - 30, (width // 2 - 42)

        def render_user_image(matrix_above, size, x, y):
            box_position = {}
            game_background = Background(screen2)
            game_background.draw_background(), flag_limit.draw_button(), lucky.draw_button()
            match.set_matrix_above(matrix_above), match.draw_number()

            for i in range(m):
                for j in range(n):
                    if matrix_above[i][j] == unknown or matrix_above[i][j] == flag:
                        button_box = GameBox(size)

                        x2, y2 = size[0] * i + x, size[1] * j + y
                        button_box.rect.x, button_box.rect.y = (x2, y2)

                        button_box.draw_game(matrix_above[i][j])

                        box_position[x2, y2] = button_box

            pygame.display.update()
            return box_position

        # Função de resposta a clicks
        def click_manager(matrix_above, size, box_position):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # CLICK ESQUERDO
                        if lucky.rect.collidepoint(event.pos):
                            if lucky.get_lucky() >= 3:
                                click = False
                                return click, matrix_above
                            function_lucky(matrix_above)

                        for position, button_box in box_position.items():
                            if button_box.rect.collidepoint(event.pos):
                                pos_x, pos_y = button_box.rect.x, button_box.rect.y

                                # Converter em posição da matrix
                                if size[0] == 50:
                                    i, j = (pos_x - 40) // 50, (pos_y - 130) // 50
                                else:
                                    i, j = (pos_x - 20) // 40, (pos_y - 115) // 40

                                if match.get_starting():
                                    match.set_starting()
                                    match.set_matrix(create_matrix(i, j))
                                    matrix_above = discover(matrix_above, i, j)

                                    return True, matrix_above

                                matrix_below = match.get_matrix()

                                if matrix_above[i][j] == flag:
                                    return False, matrix_above
                                elif matrix_below[i][j] == mine:
                                    declare_defeat()
                                else:
                                    matrix_above = discover(matrix_above, i, j)
                                    matrix_above[i][j] = empty
                                    match.set_matrix_above(matrix_above)

                        click = True
                        return click, matrix_above

                    elif event.button == 3:  # CLICK DIREITO
                        for position, button_box in box_position.items():
                            if button_box.rect.collidepoint(event.pos):
                                pos_x, pos_y = button_box.rect.x, button_box.rect.y

                                # Converter em posição da matrix
                                if size[0] == 50:
                                    i, j = (pos_x - 40) // 50, (pos_y - 130) // 50
                                else:
                                    i, j = (pos_x - 20) // 40, (pos_y - 115) // 40

                                if matrix_above[i][j] == unknown and match.get_limit_flag():
                                    matrix_above[i][j] = flag
                                    match.set_limit_flag(1)
                                    flag_limit.update_flag(1)
                                    return True, matrix_above
                                elif matrix_above[i][j] == flag:
                                    matrix_above[i][j] = unknown
                                    match.set_limit_flag(-1)
                                    flag_limit.update_flag(-1)
                                    return True, matrix_above

                                button_box.draw_game(matrix_above[i][j])
                                pygame.display.update()

                        click = False
                        return click, matrix_above

            return False, matrix_above

            # encerra loop de click e instrução para próxima ação

        def request_image_rendering_user():  # definir posição e solicita renderização
            matrix_above = [[-1] * n for _ in range(m)]
            if level:
                size_per_level = size_box_easy
                pos_x, pos_y = 40, 130
            else:
                size_per_level = size_box_hard
                pos_x, pos_y = 20, 115

            count, last_render = 0, False
            while True:
                box_position = render_user_image(matrix_above, size_per_level, pos_x, pos_y)
                last_render = declare_win(last_render)
                if last_render:
                    render_user_image(matrix_above, size_per_level, pos_x, pos_y)
                    declare_win(last_render)
                click = False
                while not click:  # repetir loop enquanto 'click' não for com botão esquerdo
                    count = limit_time(count)
                    click, matrix_above = click_manager(matrix_above, size_per_level, box_position)
                    clock.tick(delay)

        request_image_rendering_user()  # solicita argumentos de renderização da matrix


player = Player()


# >>---------------------------------- FUNÇÃO PRINCIPAL DO MENU ----------------------------------<< #


def main_game_loop():
    while True:
        action = main_menu()
        make_sound(sound_click)
        if action == "Jogar":  # Jogo
            level = difficulty_menu()
            make_sound(sound_click)
            if level is True:
                current_match(level)
            elif not level:
                current_match(level)
            elif action == "Voltar":
                main_game_loop()

        elif action == "Rank":  # Rank
            display_rank()
            make_sound(sound_click)
            if action == "Voltar":
                main_menu()

        elif action == "Sair":
            return quit_game()
        clock.tick(15)


main_game_loop()
