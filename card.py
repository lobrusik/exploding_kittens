import pygame.sprite
import math


class Card(pygame.sprite.Sprite):
    def __init__(self, name, id):
        pygame.sprite.Sprite.__init__(self)
        self.rect = None
        self.name = name
        self.id = id

    def __str__(self):
        return self.name

    def update(self):
        pass

    def play(self, game, second):
        pass

    def animate_to(self, target_pos):
        # Oblicz dystans do przesunięcia
        distance_x = target_pos[0] - self.rect.x
        distance_y = target_pos[1] - self.rect.y
        distance = math.hypot(distance_x, distance_y)

        # Oblicz ilość klatek animacji
        frames = int(distance / 10)  # Możesz dostosować prędkość animacji zmieniając wartość dzielnika

        # Oblicz prędkość poruszania się na każdej osi
        velocity_x = distance_x / frames
        velocity_y = distance_y / frames

        # Wykonaj animację
        for _ in range(frames):
            self.rect.x += velocity_x
            self.rect.y += velocity_y
            pygame.time.wait(10)  # Odstęp czasowy między klatkami animacji
            # Tutaj możesz odświeżyć ekran, aby widzieć aktualizację położenia karty

        # Wyśrodkuj kartę w celu dokładnego ustawienia na nowej pozycji
        self.rect.center = target_pos

        # Tutaj możesz zaktualizować ekran, aby karta była widoczna na nowej pozycji
