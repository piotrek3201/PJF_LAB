import pygame
from random import randint

class Player:
    def __init__(self, id, x, y, direction):
        self.id = id
        self.x = x
        self.y = y
        self.previous_x = None
        self.previous_y = None
        self.direction = direction # 0 - up, 1 - right, 2 - down, 3 - left
        self.lost = False
        self.field_x = 2
        self.field_y = 2
        self.active = False
        self.lenght = 1
        self.time = pygame.time.Clock().tick(60)
        self.tail = [TailSegment(-1, -1)]
        self.start_x = x
        self.start_y = y

    def update(self):
        keys = pygame.key.get_pressed()
        self.time += pygame.time.Clock().tick(60)

        if not self.lost:

            self.turn()

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

                # tail
                for i in range(len(self.tail) -1, -1, -1):
                    if i == 0:
                        self.tail[i].x = self.x
                        self.tail[i].y = self.y
                    else:
                        self.tail[i].x = self.tail[i - 1].x
                        self.tail[i].y = self.tail[i - 1].y

        else:

            if keys[pygame.K_r]:
                self.lost = False
                self.x = self.start_x
                self.y = self.start_y
                self.active = True

        if self.x >= 52 or self.x < 0 or self.y < 0 or self.y >= 40:
            self.lose()

    def lose(self):
        self.lost = True
        self.tail = [TailSegment(-1, -1)]
        self.lenght = 1
        self.active = False

    def turn(self):
        keys = pygame.key.get_pressed()

        if self.id == 1:
            if keys[pygame.K_RIGHT] and self.direction != 3:
                self.direction = 1
            elif keys[pygame.K_LEFT] and self.direction != 1:
                self.direction = 3
            elif keys[pygame.K_UP] and self.direction != 2:
                self.direction = 0
            elif keys[pygame.K_DOWN] and self.direction != 0:
                self.direction = 2
        elif self.id == 2:
            if keys[pygame.K_d] and self.direction != 3:
                self.direction = 1
            elif keys[pygame.K_a] and self.direction != 1:
                self.direction = 3
            elif keys[pygame.K_w] and self.direction != 2:
                self.direction = 0
            elif keys[pygame.K_s] and self.direction != 0:
                self.direction = 2


class TailSegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Fruit:
    def __init__(self):
        self.x = randint(0, 51)
        self.y = randint(0, 39)

    def eat(self):
        self.x = randint(0, 51)
        self.y = randint(0, 39)
