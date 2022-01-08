class Field:
    def __init__(self, x, y, players):
        self.x = x
        self.y = y
        self.players = list(players)
        self.used = False

    def update(self):
        unused = 0
        for i in range(len(self.players)):
            if self.players[i].active and self.players[i].field_x == self.x and self.players[i].field_y == self.y:
                self.used = True
            else:
                unused += 1
        if unused == len(self.players):
            self.used = False
