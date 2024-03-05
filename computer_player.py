from player import Player
from exploding_kitten import ExplodingKitten
from defuse import Defuse
from attack import Attack
from skip import Skip
from see_the_future import SeeTheFuture
from draw_from_bottom import DrawFromBottom
from steal import Steal
import random


class ComputerPlayer(Player):
    def __init__(self, name, image):
        super().__init__(name, image)

    def make_move(self, game):
        defuse_card = None
        for card in self.hand:
            if isinstance(card, Defuse):
                defuse_card = card
                break
        if game.hand < 10:
            game.end_turn()

        if defuse_card:
            game.play_card(self.hand.indefx(defuse_card), target_card=ExplodingKitten())
            return

        attack_card = None
        for card in self.hand:
            if isinstance(card, Attack):
                attack_card = card
                break
        if attack_card:
            game.play_card(self.hand.index(attack_card))
            return

        skip_card = None
        for card in self.hand:
            if isinstance(card, Skip):
                skip_card = card
                break
        if skip_card:
            game.play_card(self.hand.index(skip_card))
            return

        draw_from_bottom_card = None
        for card in self.hand:
            if isinstance(card, DrawFromBottom):
                draw_from_bottom_card = card
                break
        if draw_from_bottom_card:
            game.play_card(self.hand.index(draw_from_bottom_card))
            return

        see_the_future = None
        for card in self.hand:
            if isinstance(card, SeeTheFuture):
                see_the_future = card
                break
        if see_the_future:
            game.play_card(self.hand.index(see_the_future))
            return

        steal_card = None
        for card in self.hand:
            if isinstance(card, Steal):
                steal_card = card
                break
        if steal_card:
            random_player = random.choice(game.get_other_players(self))
            game.play_card(self.hand.index(steal_card), target_player=random_player)
            return

        game.end_turn()


