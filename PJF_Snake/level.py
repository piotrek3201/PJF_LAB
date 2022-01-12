import snake

class Field:
    def __init__(self, x, y, players, fruit):
        self.x = x
        self.y = y
        self.players = list(players)
        self.player_is_here = False
        self.fruit = fruit
        self.fruit_is_here = False
        self.tail_is_here = False

    def update(self):
        unused = 0
        self.tail_is_here = False



        for i in range(len(self.players)):
            if self.players[i].active and self.players[i].x == self.x and self.players[i].y == self.y:
                self.player_is_here = True

            else:
                unused += 1

            for j in range(1,len(self.players[i].tail)):
                if self.players[i].tail[j].x == self.x and self.players[i].tail[j].y == self.y:
                    self.tail_is_here = True

        if unused == len(self.players):
            self.player_is_here = False

        if self.fruit.x == self.x and self.fruit.y == self.y:
            self.fruit_is_here = True
        else:
            self.fruit_is_here = False

        if self.fruit_is_here and self.player_is_here:
            self.fruit.eat()
            self.players[0].lenght += 1
            self.players[0].tail.append(snake.TailSegment(self.players[0].tail[-1].x, self.players[0].tail[-1].y))

        if self.player_is_here and self.tail_is_here and self.players[0].lenght > 2:
            self.players[0].lose()
