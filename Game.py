import pygame
import time
import sys


class Game():
    def __init__(self) -> None:
        self.screen_width: int = 720
        self.screen_height: int = 460
        self.red: tuple[int, int, int] = pygame.Color(255, 0, 0)
        self.blue: tuple[int, int, int] = pygame.Color(0, 0, 255)
        self.black: tuple[int, int, int] = pygame.Color(0, 0, 0)
        self.white: tuple[int, int, int] = pygame.Color(255, 255, 255)
        self.fps_controller: Clock = pygame.time.Clock()
        pygame.mixer.init()
        self.music()
        self.score: int = 0
        self.background: Surface = pygame.transform.scale(pygame.image.load("The Savior.png"), (720, 460))
        self.play_surface: Surface = pygame.display.set_mode((
            self.screen_width, self.screen_height))

    def imagine(self) -> None:
        """
        Отображение изображения
        """
        self.play_surface.blit(self.background, (0, 0))

    def music(self) -> None:
        """
        Проигрыш музыки
        """
        pygame.mixer.music.load("Smooth Criminal song(SEGA remix).mp3")
        pygame.mixer.music.play(-1)

    def init_and_check_for_errors(self) -> None:
        """
        Начальная функция для инициализации и
        проверки как запустится pygame
        """
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

    def set_surface_and_title(self) -> None:
        """
        устанавливаем загаловок окна
        """
        pygame.display.set_caption('Smooth Criminal')

    def event_loop(self, change_to: str) -> str:
        """
        Функция для отслеживания нажатий клавиш игроком
        
        :param change_to: направление движения змеи
        :return: направление движения змеи
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to

    def refresh_screen(self) -> None:
        """
        обновляем экран и задаем фпс
        """
        pygame.display.flip()
        self.fps_controller.tick(24)

    def show_score(self, choice: int = 1) -> None:
        """
        Отображение результата
        
        :param choice: нужна чтобы определить как выводить результат
        :return: None
        """
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        if choice == 1:
            s_rect.midtop = (80, 10)
        else:
            s_rect.midtop = (360, 120)
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self) -> None:
        """
        Функция для вывода надписи Game Over и результатов
        в случае завершения игры и выход из игры
        """
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, self.red)
        if self.score == 100:
            go_surf2 = go_font.render('You have won', True, self.red)
        else:
            go_surf2 = go_font.render('You have lost', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        go_rect2 = go_surf.get_rect()
        go_rect2.midtop = (330, 60)
        self.play_surface.blit(go_surf, go_rect)
        self.play_surface.blit(go_surf2, go_rect2)
        self.show_score(0)
        pygame.display.flip()
        pygame.mixer.music.pause()
        time.sleep(3)
        pygame.quit()
        sys.exit()


game: Game = Game()
