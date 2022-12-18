import random, time, turtle

# Scores
pScore = 0
hScore = 0

# Window
screen = turtle.Screen()
screen.title("Simple Snake Game 🐍")
screen.bgcolor('black')

# Size of the window
screen.setup(800, 800)

# Snake
snake = turtle.Turtle()
snake.shape('square')
snake.color('white')

# No drawing
snake.penup()
snake.direction = "left"


def move():
    if snake.direction == "left":
        y = snake.ycor()
        snake.sety(y + 20)

while True:
    screen.update()
    move()
    time.sleep(1)
    