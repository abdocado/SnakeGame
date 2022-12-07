import random, time, turtle

# Scores
pScore = 0
hScore = 0

# Window
screen = turtle.Screen()
screen.title("Simple Snake Game 🐍")
screen.bgcolor('black')

# Size of the window
screen.setup(500, 500)

# Animation
screen.tracer(0)

# Snake
snake = turtle.Turtle()
snake.shape('square')
snake.color('white')

# Speed of animation, 0 being fastest
snake.speed(0)

# No drawing
snake.penup()
snake.direction = "stop"


def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)



while True:
    screen.update()

# Keep the window open
screen.mainloop()


