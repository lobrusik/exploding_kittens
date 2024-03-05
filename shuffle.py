from card import Card
import pygame
import random


class Shuffle(Card):
    def __init__(self, image):
        super().__init__("shuffle", 5)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def play(self, game, second):
        random.shuffle(game.draw_pile)
