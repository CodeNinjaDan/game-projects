import random
from turtle import Turtle, Screen
from data import colors
jon = Turtle()
screen = Screen()
screen.colormode(255)
jon.shape("arrow")
# jon.pensize(1)
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
# for _ in range(72):
#     jon.color(random.choice(colors))
#     jon.circle(100, 360, 100)
#     jon.right(5)
colours_list = [(205, 160, 84), (57, 87, 130), (145, 91, 42), (138, 27, 49), (221, 207, 110), (135, 175, 200), (155, 50, 85), (44, 55, 104), (167, 159, 42), (130, 188, 145), (83, 21, 43), (190, 139, 162), (38, 42, 65), (184, 94, 107), (87, 120, 178), (59, 38, 29), (88, 156, 93), (81, 151, 165), (194, 83, 71), (54, 127, 120), (78, 76, 44), (46, 75, 78), (45, 75, 73), (163, 200, 216), (217, 176, 188), (220, 182, 168)]
# loops = 0
# jon.home()
# for _ in range(100):
#     loops += 1
#     color_choice = random.choice(colours_list)
#     jon.dot(20, color_choice)
#     jon.penup()
#     jon.hideturtle()
#     jon.forward(50)
#     jon.showturtle()
#     jon.pendown()
#     if loops % 10 == 0:
#         jon.setx(0)
#         jon.sety(jon.ycor() + 50)
#         jon.setheading(0)

jon.penup()
jon.hideturtle()
jon.goto(-200, 200)  # Start position

for i in range(100):
    color_choice = random.choice(colours_list)
    jon.dot(20, color_choice)
    jon.forward(50)

    # Turn right and move to the next row after every 10 dots
    if (i + 1) % 10 == 0:
        jon.right(90)
        jon.forward(50)
        jon.right(90)
        jon.forward(500)
        jon.right(180)
screen.exitonclick()