import time

import pygame
import random

from card import Card
from player import Player
from computer_player import ComputerPlayer

from exploding_kitten import ExplodingKitten
from defuse import Defuse
from attack import Attack
from draw_from_bottom import DrawFromBottom
from see_the_future import SeeTheFuture
from shuffle import Shuffle
from skip import Skip
from steal import Steal


class Game:
    def __init__(self, players):
        self.players = players
        # self.current_player = random.choice(self.players)
        self.current_player_index = 0
        self.current_player = players[self.current_player_index]
        self.deck = []
        self.create_deck()
        self.discard_pile = []
        self.deck_pile = []
        self.running = True
        self.second = None

        self.game_background = pygame.image.load(r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures"
                                                 r"\2 players.png")  # Obraz tła gry
        self.discard_pile_image = pygame.image.load(
            r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\card1.png")
        self.deck_pile_image = pygame.image.load(
            r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\card1.png")

        self.dragging_card = None,
        self.drag_start_pos = (0, 0)
        self.draw_pile_rect = None

        self.font = pygame.font.Font(None, 20)
        self.option_font = pygame.font.Font(None, 20)

        self.avatar_files = [r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\player_a0.png",
                             r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\player_a1.png",
                             r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\player_a2.png"]
        self.computer_avatar_files = [
            r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\player1_a0.png",
            r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\player1_a1.png",
            r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\player1_a2.png"]

        self.current_image_index = 0
        self.image_timer = 0
        self.image_delay = 0.5

    """inicjalizacja gry: """

    def initialize_game(self):
        self.create_deck()
        self.shuffle_deck()

        self.deal_cards(6)
        for player in self.players:
            player.draw_card(Defuse(r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\defuse1.png"))
        self.deck_pile.extend(self.deck)
        self.deck = []

    """tworzenie talii"""

    def create_deck(self):
        exploding_patterns = r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\exploding_kitten.png"

        defuse_patterns = [r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\defuse1.png",
                           r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\defuse2.png",
                           r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\defuse3.png"]

        attack_patterns = r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\attack.png"

        draw_patterns = r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\draw.png"

        future_patterns = [r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\see_the_future1.png",
                           r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\see_the_future2.png"]

        shuffle_patterns = r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\shuffle.png"

        skip_patterns = [r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\skip1.png",
                         r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\skip2.png",
                         r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\skip3.png"]

        steal_patterns = [r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\steal1.png",
                          r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\steal2.png",
                          r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\steal3.png"]

        deck = [ExplodingKitten(exploding_patterns)]

        for _ in range(len(self.players) - 1):
            pattern = random.choice(defuse_patterns)
            defuse_card = Defuse(pattern)
            deck.append(defuse_card)

        for _ in range(4):
            attack_card = Attack(attack_patterns)
            deck.append(attack_card)

        for _ in range(3):
            draw_from_bottom = DrawFromBottom(draw_patterns)
            deck.append(draw_from_bottom)

        for _ in range(6):
            pattern = random.choice(future_patterns)
            see_the_future = SeeTheFuture(pattern)
            deck.append(see_the_future)

        for _ in range(5):
            shuffle_card = Shuffle(shuffle_patterns)
            deck.append(shuffle_card)

        for _ in range(9):
            pattern = random.choice(skip_patterns)
            skip_card = Skip(pattern)
            deck.append(skip_card)

        for _ in range(6):
            pattern = random.choice(steal_patterns)
            steal_card = Steal(pattern)
            deck.append(steal_card)

        self.deck = deck

    """rysowanie kart"""

    def draw_card_images(self, screen, player):
        x = 600
        y = 900
        card_width = 125
        card_height = 168
        spacing = 20

        for i, card in enumerate(player.hand):
            if isinstance(card, Card):
                # print(card)
                card_image = card.image
                card_rect = card_image.get_rect()
                card_rect.topleft = (x, y)
                screen.blit(card_image, card_rect)
                x += card_width + spacing

    """tasownie kart"""

    def shuffle_deck(self):
        random.shuffle(self.deck)

    """rozdanie kart graczom"""

    def deal_cards(self, number_of_cards):
        for player_num, player in enumerate(self.players):
            for i in range(number_of_cards):
                card = self.deck.pop(0)
                if player_num is 0:
                    card.rect.topleft = 600 + i * 145, 900
                else:
                    card.rect.topleft = -100000, -10000000
                player.draw_card(card)

    def update_card_image(self, screen):
        for card in self.current_player.hand:
            screen.blit(card.image, card.rect.x, card.rect.y)
            card.rect.x += 145

    def next_player(self):
        index = self.players.index(self.current_player)
        index = (index + 1) % len(self.players)
        self.current_player = self.players[index]

    def play_card(self, card_index):
        card = self.current_player.play_card(card_index)
        self.discard_pile.append(card)
        card.play()

    def draw_card(self):
        if self.deck:
            card = self.deck.pop(0)
            self.current_player.draw_card(card)

    def end_turn(self, or_draw_card=True):
        if or_draw_card:
            if self.deck:
                card = self.deck.pop(0)
                self.current_player.hand.append(card)
        if self.current_player.is_under_attack:
            self.current_player.attack_turns -= 1
            if self.current_player.attack_turns > 0:
                return
            self.current_player.is_under_attack = False

    def is_game_over(self):
        for player in self.players:
            if isinstance(player.hand[0], ExplodingKitten):
                return True
            return False

    def handle_card_dragging(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == pygame.BUTTON_LEFT:
                for i, card in enumerate(self.current_player.hand):
                    if card.rect.collidepoint(mouse_pos):
                        # idk co z defuse
                        if card == "steal":
                            index = self.players.index(self.current_player)
                            index = (index + 1) % len(self.players)
                            card.play(self, self.players[index])
                        else:  # attack, draw_from_bottom, exploding, see_the_future, shuffle, skip
                            print(f"lalala - {card}")
                            # card.play(self, self.second)
                        self.current_player.hand.remove(card)
                        self.discard_pile.append(card)
                        break
            elif event.button == pygame.BUTTON_RIGHT:
                if self.deck_pile_rect.collidepoint(mouse_pos):
                    if self.deck:
                        self.end_turn()

    def computer_player_turn(self):
        if not self.current_player.is_computer:
            return
        self.current_player.make_move(self)
        self.next_player()

    """Logika gry"""

    def game_loop(self):

        SCREEENSIZE = WIDTH, HEIGHT = 1920, 1080
        screen = pygame.display.set_mode(SCREEENSIZE)
        pygame.display.set_caption("Eksplodujące kotki")
        player1 = self.players[0]
        computer = self.players[1]
        self.initialize_game()

        dragging_card = False
        dragged_card = None
        drag_start_pos = None

        while self.running:
            screen.blit(self.game_background, (0, 0))

            # obrazki kart:
            self.draw_card_images(screen, player1)
            self.draw_card_images(screen, computer)

            # stos kart do zabrania
            self.deck_pile_rect = self.deck_pile[-1].image.get_rect(topleft=(612, 420))
            screen.blit(self.deck_pile_image, self.deck_pile_rect)

            # stos kart odrzuconych
            if self.discard_pile:
                top_discard_card = self.discard_pile[-1]
                self.discard_pile_rect = top_discard_card.image.get_rect(topleft=(960, 420))
                screen.blit(top_discard_card.image, self.discard_pile_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                    self.handle_card_dragging(event, screen)
            # if self.current_player_index == 0:
            #     current_images = self.avatar_files
            # else:
            #     current_images = self.computer_avatar_files
            #
            # if time.time() - self.image_timer > self.image_delay:
            #     self.current_image_index = (self.current_image_index + 1) % len(current_images)
            #     image_timer = time.time()

            # current_image = pygame.image.load(current_images[current_image_index]).convert_alpha()
            # screen.blit(current_image, (0, 0))

            card_count_text = self.font.render(f"Cards: {len(player1.hand)}", True, (255, 255, 255))
            screen.blit(card_count_text, (650, 150))

            card_count_text = self.font.render(f"Cards: {len(computer.hand)}", True, (255, 255, 255))
            screen.blit(card_count_text, (650, 850))

            # current_player = self.players[self.current_player_index]
            # self.change_player_avatar(current_player)

            # avatar_rect = current_player.avatar.get_rect(topleft=(100, 100))
            # screen.blit(current_player.avatar, avatar_rect)

            if dragging_card:
                mouse_pos = pygame.mouse.get_pos()
                delta_x = mouse_pos[0] - drag_start_pos[0]
                delta_y = mouse_pos[1] - drag_start_pos[1]
                dragged_card.rect.x += delta_x
                dragged_card.rect.y += delta_y
                drag_start_pos = mouse_pos

            pygame.display.flip()

            if len(self.current_player.hand) == 0:
                self.current_player.draw_card(self.deck)

            if self.current_player == computer:
                self.computer_player_turn()
