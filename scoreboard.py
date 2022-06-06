from turtle import Turtle


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):                           # Here we implement a scoreboard to present to the player
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.write(f"Score: {self.level}/10", align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}/10", align="left", font=FONT)

    def get_level(self):
        return self.level

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"You've Lost! You reached level {self.level}/10", align="center", font=FONT)

    def game_won(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Congratulations, you've won!", align="center", font=FONT)
