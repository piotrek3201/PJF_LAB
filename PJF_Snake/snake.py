import pygame

class Player:
    def __init__(self):
        self.x = 30
        self.y = 20
        self.direction = 1 # 0 - up, 1 - right, 2 - down, 3 - left
        self.lost = False
        self.field_x = 2
        self.field_y = 2
        self.active = False
        self.lenght = 1
        self.time = pygame.time.Clock().tick(60)

    def update(self):
        keys = pygame.key.get_pressed()
        self.time += pygame.time.Clock().tick(60)

        if not self.lost:
            if keys[pygame.K_RIGHT]:
                self.direction = 1
            elif keys[pygame.K_LEFT]:
                self.direction = 3
            elif keys[pygame.K_UP]:
                self.direction = 0
            elif keys[pygame.K_DOWN]:
                self.direction = 2

            if self.time / 1000.0 > 0.1:
                self.time = 0
                if self.direction == 0:
                    self.y -= 1
                elif self.direction == 1:
                    self.x += 1
                elif self.direction == 2:
                    self.y += 1
                elif self.direction == 3:
                    self.x -= 1

        else:
            if keys[pygame.K_r]:
                self.lost = False
                self.x = 30
                self.y = 20

        if self.x >= 52 or self.x < 0 or self.y < 0 or self.y >= 40:
            self.lost = True

