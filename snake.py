import random, time, turtle

pScore = 0
hScore = 0

# Window
screen = turtle.Screen()
screen.title("Simple Snake Game 🐍")
screen.bgcolor('black')
screen.setup(500, 500)
screen.mainloop()

# Snake
snake = turtle.Turtle()
snake.shape('square')
snake.color('white')
snake.penup()
snake.goto(0, 0)
snake.write("snake")

# Food
blob = turtle.Trutle()
blob.shape('circle')
blob.color('red')
blob.penup()
blob.goto(0, 50)

