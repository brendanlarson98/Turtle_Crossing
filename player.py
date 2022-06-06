from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()                        
        self.color("green")
        self.shape('turtle')
        self.speed(3)
        self.reset_player()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def check_is_hit(self, other):                              # Check to see if our coordinates are within range to define a "hit"
        (turtle_x, turtle_y) = self.pos()
        (other_x, other_y) = other.pos()

        if other_x >= turtle_x - 25 and other_x <= + 25 and other_y >= turtle_y - 15 and other_y <= turtle_y + 15:
            return True
        return False

    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def reset_player(self):
        self.goto(STARTING_POSITION)

