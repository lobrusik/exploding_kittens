from card import Card
import pygame


class Skip(Card):
    def __init__(self, image):
        super().__init__("skip", 3)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def play(self, game, second):
        game.end_turn(False)
        print('KONIEC!')