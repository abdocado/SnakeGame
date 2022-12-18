import random, time, turtle

# Scores
pScore = 0
hScore = 0
score = 0
body = []

# Window
screen = turtle.Screen()
screen.title("Simple Snake Game 🐍")
screen.bgcolor('black')

# Size of the window
screen.setup(800, 800)

# Smooth animation
screen.tracer(0)

# Snake
snake = turtle.Turtle()
snake.shape('square')
snake.color('white')
snake.speed(0)
snake.goto(0,0)

# No drawing
snake.penup()
snake.direction = "stop"


# Food
food = turtle.Turtle()
food.shape("circle")
food.color("orange")
food.penup()
food.speed(0)
food.goto(0, 100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

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


        # Check for a collision with the border
    if snake.xcor()>390 or snake.xcor()<-390 or snake.ycor()>390 or snake.ycor()<-390:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"
        # Hide the segments
        for segment in body:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        body.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, hScore), align="center", font=("Courier", 24, "normal")) 

    if snake.distance(food) < 18:
        x = random.randint(-390, 390)
        y = random.randint(-390, 390)
        food.goto(x, y)

        health = turtle.Turtle()
        health.speed(0)
        health.shape("square")
        health.color("blue")
        health.penup()
        body.append(health)

        score += 10
        if score >= hScore:
            hScore = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, hScore), align="center", font=("Courier", 24, "normal")) 

    
    for i in range(len(body)-1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    time.sleep(.05)
    move()


    # Check for head collision with the body segments
    for j in body:
        if j.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
        
            # Hide the segments
            for segment in body:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            body.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, hScore), align="center", font=("Courier", 24, "normal"))
 