import pygame
import os
from menu import Menu
from game import Game
from player import Player
from computer_player import ComputerPlayer

pygame.init()

SCREEENSIZE = WIDTH, HEIGHT = 1920, 1080
FPS = 60
screen = pygame.display.set_mode(SCREEENSIZE)
clock = pygame.time.Clock()

path = os.path.join(os.pardir, r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures")
file_names = sorted(os.listdir(path))
file_names.remove('background.png')
BACKGROUND = pygame.image.load(os.path.join(path, r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures"
                                                  r"\background.png")).convert()
IMAGES = {}
for file_name in file_names:
    IMAGES[file_name[:-4].upper()] = pygame.image.load(
        os.path.join(path, file_name)).convert_alpha()

if __name__ == "__main__":
    player_image = [r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\player_a0.png",
                    r"C:\Users\lobru\OneDrive\Pulpit\eksplodujace_kotki\próba3\pictures\player1_a0.png"]
    players = [Player("Player 1", player_image[0]),ComputerPlayer("Computer", player_image[1])]

    game = Game(players)
    menu = Menu(screen, WIDTH, HEIGHT)
    menu_running = True

    while menu_running:
        menu.draw_menu()
        number_of_players = menu.handle_events()

        if number_of_players == 2:
            print(number_of_players)
            game.game_loop()
            menu_running = False

pygame.display.flip()
clock.tick(FPS)

pygame.quit()

while menu_runing:
    menu_draw_menu()
    number of members = menu.handle_events()