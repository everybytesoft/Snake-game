import pygame
import random
import copy
from Game import Game


class Savior():
    def __init__(self, savior_color: str) -> None:
        """
        Инит змеи
        
        :param savior_color: цвет змеи
        :return: None
        """
        # важные переменные - позиция головы змеи и его тела
        self.savior_head_pos: List[int] = [100, 50]  # [x, y]
        # начальное тело змеи состоит из трех сегментов
        # голова змеи - первый элемент, хвост - последний
        self.savior_body: List[List[int]] = [[100, 50], [90, 50], [80, 50]]
        self.savior_color: str = savior_color
        # направление движение змеи, изначально
        # зададимся вправо
        self.direction: str = "RIGHT"
        # куда будет меняться направление движения змеи
        # при нажатии соответствующих клавиш
        self.change_to: str = self.direction

    def validate_direction_and_change(self) -> None:
        """
        изменияем направление движения змеи только в том случае,
        если оно не прямо противоположно текущему
        """
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head_position(self) -> None:
        """
        изменияем положение головы змеи
        """
        if self.direction == "RIGHT":
            self.savior_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.savior_head_pos[0] -= 10
        elif self.direction == "UP":
            self.savior_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.savior_head_pos[1] += 10

    def savior_body_mechanism(self, score: int, criminal_pos: list[int], screen_width: int, screen_height: int) -> tuple[int, list[int]]:
        """
        Механизм движения змеи
        
        :param score: счет игрока
        :param criminal_pos: позиция еды
        :param screen_width: ширина экрана
        :param screen_height: длина экрана
        :return: счет и позицию еды
        """
        # если вставлять просто savior_head_pos,
        # то на всех трех позициях в savior_body
        # окажется один и тот же список с одинаковыми координатами
        # и мы будем управлять змеей из одного квадрата
        head_pos_copy = copy.deepcopy(self.savior_head_pos)
        self.savior_body.insert(0, head_pos_copy)
        # если съели еду
        if (self.savior_head_pos[0] == criminal_pos[0]
                and self.savior_head_pos[1] == criminal_pos[1]):
            # если съели еду то задаем новое положение еды случайным образом
            # и увеличивем score на один
            criminal_pos = [random.randrange(1, screen_width / 10) * 10,
                            random.randrange(1, screen_height / 10) * 10]
            score += 1
        self.savior_body.pop()
        return score, criminal_pos

    def draw_savior(self, play_surface: pygame.Surface, surface_color: tuple[int, int, int]) -> None:
        """
        Отображаем все сегменты змеи
        
        :param play_surface: поверхность игры
        :param surface_color: цвет змеи
        :return: None
        """
        play_surface.fill(surface_color)
        # здесь отображаем изображение, чтобы оно ничего не перекрывало
        game.imagine()
        for pos in self.savior_body:
            # pygame.rect(x, y, sizex, sizey)
            pygame.draw.rect(
                play_surface, self.savior_color, pygame.Rect(
                    pos[0], pos[1], 10, 10))

    def check_for_boundaries(self, game_over: callable, screen_width: int, screen_height: int, score: int) -> None:
        """
        проверка, что столкунлись с концами экрана
        
        :param game_over: функция
        :param screen_width: ширина экрана
        :param screen_height: длина экрана
        :param score: счет игрока
        :return: None
        """
        if any((
            self.savior_head_pos[0] > screen_width - 10
            or self.savior_head_pos[0] < 0,
            self.savior_head_pos[1] > screen_height - 10
            or self.savior_head_pos[1] < 0
        )):
            game_over()
        if game.score == 100:
            game_over()


class Criminal():
    def __init__(self, criminal_color: str, screen_width: int, screen_height: int) -> None:
        """
        Инит еды
        
        :param criminal_color: цвет змеи
        :param screen_width: ширина экрана
        :param screen_height: длина экрана
        :return: None
        """
        self.criminal_color = criminal_color
        self.criminal_size_x: int = 10
        self.criminal_size_y: int = 10
        self.criminal_pos: list = [random.randrange(1, screen_width / 10) * 10, random.randrange(1, screen_height / 10) * 10]

    def draw_criminal(self, play_surface: pygame.Surface) -> None:
        """
        Отображение еды
        
        :param play_surface: поверхность игры
        :return: None
        """
        pygame.draw.rect(
            play_surface, self.criminal_color, pygame.Rect(
                self.criminal_pos[0], self.criminal_pos[1], self.criminal_size_x, self.criminal_size_y))


game: Game = Game()
savior: Savior = Savior(game.blue)
criminal: Criminal = Criminal(game.black, game.screen_width, game.screen_height)
