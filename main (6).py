from Game import Game
from Personages import Savior, Criminal

game: Game = Game()
savior: Savior = Savior(game.blue)
criminal: Criminal = Criminal(game.black, game.screen_width, game.screen_height)

game.init_and_check_for_errors()
game.set_surface_and_title()

while True:
    savior.change_to = game.event_loop(savior.change_to)

    savior.validate_direction_and_change()
    savior.change_head_position()

    game.score, criminal.criminal_pos = savior.savior_body_mechanism(
        game.score, criminal.criminal_pos, game.screen_width, game.screen_height)
    savior.draw_savior(game.play_surface, game.white)

    criminal.draw_criminal(game.play_surface)

    savior.check_for_boundaries(
        game.game_over, game.screen_width, game.screen_height, game.score)

    game.show_score()
    game.refresh_screen()
