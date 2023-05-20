from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win race?:choose a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-80, -50, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x=-280, y=y_position[turtle_index])
    all_turtles.append(new_turtles)

is_race_on = True

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 265:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
               print(f"you have won! the {wining_color} turtle is winner")
            else:
                print(f"you have lost! the {wining_color} turtle is winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()