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
snake.direction = "stop"

def up():
    snake.direction = "up"

def down():
    snake.direction = "down"

def right():
    snake.direction = "right"

def left():
    snake.direction = "left"

screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")

def move():
    x = snake.xcor()
    y = snake.ycor()
    if snake.direction == "left":
        snake.setx(x - 20)

    if snake.direction == "right":
        snake.setx(x + 20)

    if snake.direction == "up":
        snake.sety(y + 20)

    if snake.direction == "down":
        snake.sety(y - 20)


while True:
    screen.update()
    move()
    time.sleep(1)
