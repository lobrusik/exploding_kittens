def start_dragging_card(self, mouse_pos):
    x = 960
    y = 540
    card_width = 125
    card_height = 168
    spacing = 20
    # przejście przez karty w ręce gracza
    for i, card in enumerate(self.current_player.hand):
        card_rect = card.image.get_rect()
        card_rect.topleft = (x + i * (card_width + spacing), y)
        # czy kursor myszy jest na karcie
        if card_rect.collidepoint(mouse_pos):
            # przypisanie karty do karty, którą przeciągamy
            self.dragging_card = card
            # usunięcie karty z ręki gracza
            self.dragging_card = self.current_player.hand.pop(i)
            # pozycja początkowa przeciągania
            self.drag_start_pos = mouse_pos
            break
    # #stos kart do pobrania
    self.draw_pile_rect = self.deck_pile_image.get_rect(topleft=(612, 420))
    # czy pozycja mysz jest na stosie kart
    if self.draw_pile_rect.collidepoint(mouse_pos) and not self.dragging_card:
        # pobranie karty ze stosu
        self.draw_card()

    # czy gracz odrzucił kartę?
    discard_pile_rect = self.discard_pile_image.get_rect(topleft=(x, y))
    if discard_pile_rect.collidepoint(mouse_pos) and self.dragging_card:
        # karta zostaje odrzucona
        self.discard_pile.append(self.dragging_card)
        # wykonanie akcji karty
        self.dragging_card.action(self.dragging_card)
        # reset
        self.dragging_card = None

# def update_dragged_card_position(self, mouse_pos):
#     if self.dragging_card:
#         self.dragging_card.x = mouse_pos[0]
#         self.dragging_card.y = mouse_pos[1]
#     # dx = mouse_pos[0] - drag_start_pos[0]
#     # dy = mouse_pos[1] - drag_start_pos[1]
#     # dragged_card.rect.x += self.dragging_card.x
#     # dragged_card.rect.y += dy
#
# def end_dragging_card(self, mouse_pos):
#     if self.dragging_card:
#         discard_pile_rect = self.discard_pile_image.get_rect(center=(612, 600))  # zmiana z 960, 250
#         if discard_pile_rect.collidepoint(mouse_pos):
#             self.discard_pile.append(self.dragging_card)
#             self.dragging_card.play()
#         else:
#             self.current_player.hand.append(self.dragging_card)
#
#         self.dragging_card = None
#         self.drag_start_pos = (0, 0)
#
# def draw_dragged_card(self, screen, mouse_pos):
#     # if self.dragging_card:
#     #     dragging_card_rect = self.dragging_card.image.get_rect(center=mouse_pos)
#     #     screen.blit(self.dragging_card.image, dragging_card_rect)
#     card_rect = self.dragging_card.image.get_rect()
#     card_rect.x = self.start_dragging_card[0]
#     card_rect.y = self.start_dragging_card[1]
#     discard_pile_rect = self.discard_pile_image.get_rect(topleft=(300, 500))
#     screen.blit(self.dragging_card.image, card_rect)
#     if card_rect.colliderect(discard_pile_rect):
#         self.discard_pile.append(self.dragging_card)
#         self.dragging_card.play()
#     else:
#         self.current_player.hand.append(self.dragging_card)
#         self.dragging_card.animate_to(mouse_pos)  # Dodaj animację
