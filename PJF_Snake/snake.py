import pygame

class Player:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.direction = 1 # 0 - up, 1 - right, 2 - down, 3 - left

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction = 1
        elif keys[pygame.K_LEFT]:
            self.direction = 3
        elif keys[pygame.K_UP]:
            self.direction = 0
        elif keys[pygame.K_DOWN]:
            self.direction = 2

        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1
