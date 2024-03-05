from card import Card
import pygame


class Defuse(Card):
    def __init__(self, image):
        super().__init__("defuse", 1)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def play(self, game, defuse_card):
        #do stosu odrzuconych kart
        game.discard_pile.append(defuse_card)
        exploding_kitten = None
        for card in game.draw_pile:
            if card.name == "exploding_kitten":
                exploding_kitten = card
                break
            if exploding_kitten:
                game.draw_pile.remove(exploding_kitten) #usuń kota
                game.draw_pile.append(exploding_kitten) #dodaj kota
                game.end_turn(False) #koniec tury bez losowania
