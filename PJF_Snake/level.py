import snake

class Field:
    def __init__(self, x, y, players, fruit):
        self.x = x
        self.y = y
        self.players = list(players)
        self.player_is_here = [False, False]
        self.fruit = fruit
        self.fruit_is_here = False
        self.tail_is_here = [False, False]

    def update(self):
        self.tail_is_here = [False, False]
        self.player_is_here = [False, False]

        for i in range(len(self.players)):
            #snakes' heads
            if self.players[i].active and self.players[i].x == self.x and self.players[i].y == self.y:
                self.player_is_here[i] = True

            #snakes' tails
            for j in range(1,len(self.players[i].tail)):
                if self.players[i].tail[j].x == self.x and self.players[i].tail[j].y == self.y:
                    self.tail_is_here[i] = True

            #collision with own tail
            if self.player_is_here[i] and self.tail_is_here[i] and self.players[i].lenght > 2:
                self.players[i].lose()

            #collision with other snakes
            for j in range(len(self.players)):
                if j != i:
                    if self.players[i].active and self.players[j].x == self.players[i].x and self.players[j].y == self.players[i].y:
                        self.players[i].lose()
                        self.players[j].lose()
                    for k in range(1,len(self.players[j].tail)):
                        if self.players[i].active and self.players[j].tail[k].x == self.players[i].x and self.players[j].tail[k].y == self.players[i].y:
                            self.players[i].lose()

            #snake eats the fruit
            if self.fruit_is_here and self.player_is_here[i]:
                self.fruit.eat()
                self.players[i].lenght += 1
                self.players[i].tail.append(snake.TailSegment(self.players[i].tail[-1].x, self.players[i].tail[-1].y))

        #fruit
        if self.fruit.x == self.x and self.fruit.y == self.y:
            self.fruit_is_here = True
        else:
            self.fruit_is_here = False




