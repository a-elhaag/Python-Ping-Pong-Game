import turtle
import random

# Window
window = turtle.Screen()
window.title('Ping Pong')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

# Score
anas_score = 0
unknown_score = 0

# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('red')
right_paddle.penup()
right_paddle.goto(350, 0)
right_paddle.shapesize(stretch_wid=6, stretch_len=0.5)

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('blue')
left_paddle.penup()
left_paddle.goto(-350, 0)
left_paddle.shapesize(stretch_wid=6, stretch_len=0.5)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx= random.uniform(-0.15, 0.15)  # Randomly select a number from the range -0.15 to 0.15 for horizontal movement
ball.dy= random.uniform(-0.15, 0.15)  # Randomly select a number from the range -0.15 to 0.15 for vertical movement

# Panel
panel = turtle.Turtle()
panel.speed(0)
panel.color('white')
panel.penup()
panel.hideturtle()
panel.goto(0, 260)
panel.write('Anas: 0 - 0 :UNKNOWN', align='center', font=('Courier', 24, 'normal'))

# Paddle Movement
def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Keyboard Binding
window.listen()
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')

# Main Game Loop
while True:
    window.update()

    # Ball Movement
    next_x = ball.xcor() + ball.dx
    next_y = ball.ycor() + ball.dy
    ball.setx(next_x)
    ball.sety(next_y)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball hitting the goal
    if ball.xcor() > 390:
        anas_score += 1
        panel.clear()
        panel.write('Anas: {} - {} :UNKNOWN'.format(anas_score, unknown_score), align='center', font=('Courier', 24, 'normal'))
        
        #Ball Coordinates
        ball.dx = random.uniform(-0.15, 0.15)  # Randomly select a number from the range -0.15 to 0.15 for horizontal movement
        ball.dy = random.uniform(-0.15, 0.15)  # Randomly select a number from the range -0.15 to 0.15 for vertical movement

        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -390:
        unknown_score += 1
        panel.clear()
        panel.write('Anas: {} - {} :UNKNOWN'.format(anas_score, unknown_score), align='center', font=('Courier', 24, 'normal'))
        #Ball Coordinates
        ball.dx = random.uniform(-0.15, 0.15)  # Randomly select a number from the range -0.15 to 0.15 for horizontal movement
        ball.dy = random.uniform(-0.15, 0.15)  # Randomly select a number from the range -0.15 to 0.15 for vertical movement

        ball.goto(0, 0)
        ball.dx *= -1

    # Ball hitting the paddle
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40:
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40:
        ball.dx *= -1
