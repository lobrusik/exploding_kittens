from card import Card
import pygame


class DrawFromBottom(Card):
    def __init__(self, image):
        super().__init__("draw_from_bottom", 6)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def play(self, game, second):
        drawn_card = game.draw_pile.pop(-1)
        game.current_player.hand.append(drawn_card)
        game.end_turn(False)
