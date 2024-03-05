from card import Card
import pygame


class Attack(Card):
    def __init__(self, image):
        super().__init__("attack", 2)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def play(self, game, second = None):
        game.end_turn(False)
        next_player_index = (game.player.index(game.current_player) + 1 % len(game.player))
        next_player = game.player[next_player_index]
        next_player.is_under_attack = True

