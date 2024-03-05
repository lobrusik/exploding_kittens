from card import Card
import pygame


class Steal(Card):
    def __init__(self, image):
        super().__init__("steal", 7)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def play(self, game, target_player):
        if target_player not in game.players or target_player == game.current_player:
            return
        chosen_card = target_player.choose_card_to_give()
        if chosen_card is None or chosen_card not in target_player.hand:
            return
        target_player.hand.remove(chosen_card)
        game.current_player.hand.append(chosen_card)
