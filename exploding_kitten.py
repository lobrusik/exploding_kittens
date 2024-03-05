from card import Card
from player import Player
from defuse import Defuse
import pygame


class ExplodingKitten(Card):
    def __init__(self, image):
        super().__init__("exploring kitten", 0)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def play(self, player, second = None):
        if player.has_defuse():
            player.use_defuse()
        else:
            text = "Przegrales"
