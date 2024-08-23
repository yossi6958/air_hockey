import pygame


class GameTimer:
    def __init__(self, duration):
        self.duration = duration  # Duration in seconds
        self.start_time = 0
        self.elapsed_time = 0
        self.paused_time = 0
        self.paused = False
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = pygame.time.get_ticks()
            self.running = True
            self.paused = False

    def pause(self):
        if self.running and not self.paused:
            self.paused_time += pygame.time.get_ticks() - self.start_time
            self.paused = True

    def resume(self):
        if self.running and self.paused:
            self.start_time = pygame.time.get_ticks() - self.paused_time
            self.paused = False

    def reset(self):
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0
        self.paused_time = 0
        self.paused = False
        self.running = True

    def get_remaining_time(self):
        if not self.running:
            return 0
        if self.paused:
            elapsed = self.paused_time
        else:
            elapsed = pygame.time.get_ticks() - self.start_time
        return max(0, self.duration - (elapsed / 1000.0))

    def draw(self, surface, font):
        remaining_time = int(self.get_remaining_time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_text = font.render(f"{minutes}:{seconds:02}", True, (0, 0, 0))
        surface.blit(timer_text, [surface.get_width() / 2 - timer_text.get_width() - 100 / 2, 10])
