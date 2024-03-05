from card import Card
import pygame


class SeeTheFuture(Card):
    def __init__(self, image):
        super().__init__("see_the_future", 4)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def play(self, game, second):
        if len(game.draw_pile) >= 3:
            top_cards = game.draw_pile[:3]
            game.draw_pile = top_cards + game.draw_pile[3:]
        else:
            top_cards = game.draw_pile[:len(game.draw_pile)]
            game.current_player.show_cards(top_cards)
            game.draw_pile = top_cards + game.draw_pile[len(game.draw_pile):  ]

