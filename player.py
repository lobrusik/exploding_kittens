import pygame
from defuse import Defuse


class Player(pygame.sprite.Sprite):
    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image = image
        self.hand = []
        self.defuse_card = 1

    def draw_card(self, card):
        self.hand.append(card)

    def play_card(self, card_index):
        card = self.hand.pop(card_index)
        return card

    def has_defuse(self):
        return self.defuse_card > 0

    def use_defuse(self, defuse):
        defuse.play()
