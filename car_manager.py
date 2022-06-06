from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = 1
        
        for i in range(10):                                 # create some cars so our screen isn't empty
            random_int = random.randint(0,300)
            self.create_car(random_int)
        
    def create_car(self, x=300):                            # Here we define a function to create our cars, which will appear randomly across the "street"
        car = Turtle("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.goto(x=x, y=random.randint(-250, 250))
        car.speed(self.speed)
        self.all_cars.append(car)

    def move_cars(self):                
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)

    def get_cars(self):
        return self.all_cars

    def new_level(self):     
        self.speed += 1                                   # When we create a level, increase speed of each car. 
        
    def maybe_make_car(self):                             # So we arent' inundated with cars, reduce chance of making a car.
        chance_car = random.randint(1,4)
        if chance_car == 1:
            self.create_car()

    def delete_cars(self):                                # So we don't have cars still running off to the side, 
        for car in self.all_cars:
            if car.xcor() < -300:
                car.clear()
                car.hideturtle()
                self.all_cars.remove(car)
