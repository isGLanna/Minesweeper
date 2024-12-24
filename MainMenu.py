from AbstractMenu import *


class MainMenu(AbstractMenu):
    def __init__(self, width, height, background):
        super.__init__(self)
        self.width = width
        self.height = height
        self.background = background

        self.button_start = Buttons("Jogar", (200, 60), button1, button2, font_0)
        self.button_rank = Buttons("Rank", (200, 60), button1, button2, font_0)
        self.button_exit = Buttons("Sair", (200, 60), button1, button2, font_0)

        self.button_start.rect.y, self.button_start.rect.x = (height - 60) // 2 - 125, (width - 200) // 2
        self.button_rank.rect.y, self.button_rank.rect.x = (height - 60) // 2, (width - 200) // 2
        self.button_exit.rect.y, self.button_exit.rect.x = (height - 60) // 2 + 125, (width - 200) // 2

    def draw_background(self):
        self.background.draw.background()
        self.background.transparent_surface()

    def buttons(self):
        return [self.button_start, self.button_rank, self.button_exit]

    def show(self):
        self.draw_background()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.quitting()

                if event.type == pygame.MOUSEBUTTONUP:
                    clicked_button = self.get_events()

                    if clicked_button == self.button_start:
                        clicked_button.up()
                        make_sound(sound_click)
                        game = DifficultyMenu()
                        game.show()

                    elif clicked_button == self.button_rank:
                        clicked_button.up()
                        make_sound(sound_click)
                        game = RankMenu()
                        game.show()

                    elif clicked_button == self.button_exit:
                        clicked_button.up()
                        make_sound(sound_click)
                        self.quitting()

            self.button_start.print_display(pygame.mouse.get_pos())
            self.button_rank.print_display(pygame.mouse.get_pos())
            self.button_exit.print_display(pygame.mouse.get_pos())
            pygame.display.update()
            clock.tick(60)

