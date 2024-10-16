import random
from turtle import Turtle, Screen
from data import colors
jon = Turtle()
jon.shape("arrow")
jon.pensize(1)
jon.speed(10)


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         jon.forward(100)
#         jon.right(angle)

#Move the turtle in random directions and draw randomly

# for shape in range(3,11):
#     jon.color(choice(colors))
#     draw_shape(shape)
# def random_move(turtle):
#     for _ in range(50):
#         jon.color(random.choice(colors))
#         angle = 90
#         distance = random.randint(-20, 75)
#         turtle.right(angle)
#         turtle.forward(distance)
# random_move(jon)

#Draw a Spirograph
for _ in range(72):
    jon.color(random.choice(colors))
    jon.circle(100, 360, 100)
    jon.right(5)

screen = Screen()
screen.exitonclick()