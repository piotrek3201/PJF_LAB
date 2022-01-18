import pygame
from random import randint

def random_direction(d1, d2):
    rand = randint(0, 1)
    if rand == 0:
        return d1
    else:
        return d2

class Player:
    def __init__(self, id, x, y, direction, fruit):
        self.id = id
        self.x = x
        self.y = y
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
        self.cpu = False
        self.fruit = fruit
        self.other_players = None
        self.others = []

    def update(self):
        keys = pygame.key.get_pressed()
        self.time += pygame.time.Clock().tick(60)

        if not self.lost:

            if not self.cpu:
                self.turn()

            if self.time / 1000.0 > 0.03:

                if self.cpu:
                    self.cpu_turn()

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
                self.restart()

        if self.x >= 52 or self.x < 0 or self.y < 0 or self.y >= 40:
            self.lose()

    def lose(self):
        self.x = -1
        self.y = -1
        self.lost = True
        self.tail = [TailSegment(-1, -1)]
        self.active = False

    def restart(self):
        self.lost = False
        self.x = self.start_x
        self.y = self.start_y
        self.active = True
        self.lenght = 1

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

    def cpu_turn(self):
        fruit_x = self.fruit.x
        fruit_y = self.fruit.y

        self.others = []

        pr_dir = self.direction

        # collision detection with other snakes

        for i in self.other_players:
            if i.active:
                if i.id != self.id:
                    self.others.append((i.x, i.y))
                for j in i.tail:
                    self.others.append((j.x, j.y))


        # 0 - up, 1 - right, 2 - down, 3 - left

        if fruit_x > self.x and pr_dir != 3 and (self.x+1, self.y) not in self.others:
            self.direction = 1
        elif fruit_x < self.x and pr_dir != 1 and (self.x-1, self.y) not in self.others:
            self.direction = 3
        elif fruit_y < self.y and pr_dir != 2 and (self.x, self.y-1) not in self.others:
            self.direction = 0
        elif fruit_y > self.y and pr_dir != 0 and (self.x, self.y+1) not in self.others:
            self.direction = 2

        if fruit_x == self.x and fruit_y < self.y and pr_dir == 2 and 0 < self.x < 51:
            self.direction = random_direction(1, 3)
        elif fruit_y == self.y and fruit_x < self.x and pr_dir == 3 and 0 < self.y < 39:
            self.direction = random_direction(0, 2)
        elif fruit_x == self.x and fruit_y > self.y and pr_dir == 0 and 0 < self.x < 51:
            self.direction = random_direction(1, 3)
        elif fruit_y == self.y and fruit_x > self.x and pr_dir == 1 and 0 < self.y < 39:
            self.direction = random_direction(0, 2)

        # 0 - up, 1 - right, 2 - down, 3 - left
        if pr_dir == 1 and (self.x + 1, self.y) in self.others and (self.x, self.y-1) not in self.others and self.y > 0:
            self.direction = 0
        elif pr_dir == 1 and (self.x + 1, self.y) in self.others and (self.x, self.y+1) not in self.others and self.y < 39:
            self.direction = 2
        elif pr_dir == 3 and (self.x - 1, self.y) in self.others and (self.x, self.y-1) not in self.others and self.y > 0:
            self.direction = 0
        elif pr_dir == 3 and (self.x - 1, self.y) in self.others and (self.x, self.y+1) not in self.others and self.y < 39:
            self.direction = 2
        elif pr_dir == 2 and (self.x, self.y + 1) in self.others and (self.x - 1, self.y) not in self.others and self.x > 0:
            self.direction = 3
        elif pr_dir == 2 and (self.x, self.y + 1) in self.others and (self.x + 1, self.y) not in self.others and self.x < 51:
            self.direction = 1
        elif pr_dir == 0 and (self.x, self.y - 1) in self.others and (self.x - 1, self.y) not in self.others and self.x > 0:
            self.direction = 3
        elif pr_dir == 0 and (self.x, self.y - 1) in self.others and (self.x + 1, self.y) not in self.others and self.x < 51:
            self.direction = 1


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
