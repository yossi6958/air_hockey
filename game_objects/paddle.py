import math

import pygame

from constants import constants


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = constants.PADDLE_SIZE
        self.speed = constants.PADDLE_SPEED
        self.mass = constants.PADDLE_MASS
        self.angle = 0

    def check_vertical_bounds(self, height):
        # Top boundary
        if self.y - self.radius <= 0:
            self.y = self.radius
        # Bottom boundary
        elif self.y + self.radius > height:
            self.y = height - self.radius

    def check_left_boundary(self, width):
        if self.x - self.radius <= 0:
            self.x = self.radius
        elif self.x + self.radius > int(width / 2):
            self.x = int(width / 2) - self.radius

    def check_right_boundary(self, width):
        if self.x + self.radius > width:
            self.x = width - self.radius
        elif self.x - self.radius < int(width / 2):
            self.x = int(width / 2) + self.radius

    def move_keyboard(self, up, down, left, right, time_delta):
        dx, dy = self.x, self.y
        self.x += (right - left) * self.speed * time_delta
        self.y += (down - up) * self.speed * time_delta

        # Calculate angle of movement
        dx = self.x - dx
        dy = self.y - dy
        self.angle = math.atan2(dy, dx)

    def move_mouse(self, mouse_x, mouse_y):
        # Update paddle's position to follow mouse (centering it on the mouse)
        self.x = mouse_x
        self.y = mouse_y

    def draw(self, screen, color):
        position = (int(self.x), int(self.y))
        pygame.draw.circle(screen, color, position, self.radius, 0)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius, 2)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius - 5, 2)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius - 10, 2)

    def get_pos(self):
        return self.x, self.y

    def reset(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
