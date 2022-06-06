import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)                                            # In order for our animation to run smoothly, turn off our updating unless we manually update
turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

screen.update()

game_is_on = True
while game_is_on:
    if turtle.finish():                                     # If our turtle finishes, we go to our next level. Max level is 11
        scoreboard.next_level()
        if scoreboard.get_level() == 11:
            game_is_on = False
            scoreboard.game_won()
            break

        cars.new_level()
        turtle.reset_player()

    cars.move_cars()
    cars.maybe_make_car()

    for car in cars.get_cars():                             # For each car, check if we are roadkill.
        if turtle.check_is_hit(car):
            game_is_on = False
            scoreboard.game_over()
            break
    
    cars.delete_cars()
    
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
