import os
import random as rand
import sys

import pygame

from screens.startScreen import disp_text, button_circle
from utils.globals import colors, width, height, buttonRadius, auxDirectory


# Game end screen function
def game_end(screen: pygame.Surface, clock: pygame.time.Clock, background_color: tuple[int, int, int],
             player_name: str) -> int:
    celeb_text = pygame.font.Font(os.path.join(auxDirectory, 'MR ROBOT.ttf'), 140)
    large_text = pygame.font.Font('freesansbold.ttf', 45)
    small_text = pygame.font.Font('freesansbold.ttf', 30)

    while True:
        screen.fill(background_color)

        # Set flashing colors
        color_x = rand.randint(0, 4)
        color_y = rand.randint(0, 1)

        # Get inputs
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 1  # Reset game
                elif event.key == pygame.K_m:
                    return 2  # Go to menu
                elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Display which player won
        disp_text(screen, f"{player_name.upper()} WINS", (width / 2, height / 2 - 150), celeb_text,
                  colors[color_x][color_y])

        # Drawing buttons for reset, menu, and exit
        # Reset button
        if abs(mouse_pos[0] - 200) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            button_circle(screen, colors[0][0], (200, 470), "Reset", large_text, (255, 255, 255),
                          (width / 2 - 400, height / 2 + 170))
            if mouse_press[0] == 1:
                return 1
        else:
            button_circle(screen, colors[0][0], (200, 470), "Reset", small_text, (255, 255, 255),
                          (width / 2 - 400, height / 2 + 170))

        # Menu button
        if abs(mouse_pos[0] - 600) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            button_circle(screen, colors[4][1], (600, 470), "Menu", large_text, (255, 255, 255),
                          (width / 2, height / 2 + 170))
            if mouse_press[0] == 1:
                return 2
        else:
            button_circle(screen, colors[4][1], (600, 470), "Menu", small_text, (255, 255, 255),
                          (width / 2, height / 2 + 170))

        # Quit button
        if abs(mouse_pos[0] - 1000) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            button_circle(screen, colors[1][1], (1000, 470), "Quit", large_text, (255, 255, 255),
                          (width / 2 + 400, height / 2 + 170))
            if mouse_press[0] == 1:
                pygame.quit()
                return 3
        else:
            button_circle(screen, colors[1][0], (1000, 470), "Quit", small_text, (255, 255, 255),
                          (width / 2 + 400, height / 2 + 170))

        pygame.display.update()
        clock.tick(10)
