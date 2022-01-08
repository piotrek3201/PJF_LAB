import pygame

class Player:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.direction = 1 # 0 - up, 1 - right, 2 - down, 3 - left
        self.lost = False
        self.field_x = 2
        self.field_y = 2
        self.active = False
        self.lenght = 1

    def update(self):
        keys = pygame.key.get_pressed()

        if not self.lost:
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

            self.field_x = self.compute_field_x()
            self.field_y = self.compute_field_y()
        else:
            if keys[pygame.K_r]:
                self.lost = False
                self.x = 30
                self.y = 30

        if self.x > 790 or self.x < 10 or self.y < 10 or self.y > 610:
            self.lost = True

    def compute_field_x(self):
        a = range(10, 790+30, 15)
        for i in range(len(a)-1):
            if self.x >= a[i] and self.x < a[i+1]:
                return i

    def compute_field_y(self):
        a = range(10, 610+30, 15)
        for i in range(len(a)-1):
            if self.y >= a[i] and self.y < a[i+1]:
                return i