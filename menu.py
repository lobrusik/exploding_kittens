import pygame
import sys

WHITE = (255, 255, 255)
class Menu:

    def __init__(self, screen, WIDTH, HEIGHT):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.font = pygame.font.Font(None, 60)
        self.option_font = pygame.font.Font(None, 60)
        self.background = pygame.image.load(r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures"
                                            r"\background.png")

        self.text = self.option_font.render("Gramy!", True, WHITE)
        self.rect = self.text.get_rect(center=(WIDTH//2, HEIGHT//2))

    def draw_menu(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text, self.rect)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    return 2
        return None
