from GameMachine import GameMachine
from ButtonTypes import *
from Settings import *


def current_match(level, player):  # Função interna do jogo campo minado

    match = GameMachine(level, player)

    while True:
        # >>---------------------------------- FUNÇÃO INTERNA DE JOGO ----------------------------------<< #

        # Geração do campo minado
        m, n, bomb = match.difficulty()

        flag_limit = GenericButtons((35, 35), flag_image, False, (match.get_bombs() - match.get_number_flag()))
        flag_limit.rect.x, flag_limit.rect.y = 70, 60

        def render_user_image(matrix_above, size, x, y):
            box_position = {}
            game_background = Background(screen2)
            game_background.draw_background(), flag_limit.draw_button(), match.lucky.draw_button()
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
                        if match.lucky.rect.collidepoint(event.pos):
                            if match.lucky.get_lucky() >= 3:
                                click = False
                                return click, matrix_above
                            match.function_lucky()

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
                                    match.create_matrix(i, j)
                                    match.discover(i, j)
                                    matrix_above = match.get_matrix_above()

                                    return True, matrix_above

                                matrix_below = match.get_matrix()

                                if matrix_above[i][j] == flag:
                                    return False, matrix_above
                                elif matrix_below[i][j] == mine:
                                    return match.declare_defeat(), 0
                                else:
                                    match.discover(i, j)
                                    matrix_above = match.get_matrix_above()
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
                last_render = match.declare_win(last_render)
                if last_render:
                    render_user_image(matrix_above, size_per_level, pos_x, pos_y)
                    return match.declare_win(last_render)
                click = False
                while not click:  # repetir loop enquanto 'click' não for com botão esquerdo
                    count = match.limit_time(count)
                    click, matrix_above = click_manager(matrix_above, size_per_level, box_position)
                    if click == "Restart":
                        return click
                    clock.tick(delay)

        return request_image_rendering_user()  # solicita argumentos de renderização da matrix
