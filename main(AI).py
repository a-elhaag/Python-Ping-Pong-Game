import turtle
import random
import math

# Window
window = turtle.Screen()
window.title('Ping Pong')
window.bgcolor('black')
window.setup(width=900, height=700)
window.tracer(0)

# Score
player_score = 0
ai_score = 0

# Right Paddle (Player)
player_paddle = turtle.Turtle()
player_paddle.speed(0)
player_paddle.shape('square')
player_paddle.color('red')
player_paddle.penup()
player_paddle.goto(350, 0)
player_paddle.shapesize(stretch_wid=6, stretch_len=0.5)

# Left Paddle (AI)
ai_paddle = turtle.Turtle()
ai_paddle.speed(0)
ai_paddle.shape('square')
ai_paddle.color('green')
ai_paddle.penup()
ai_paddle.goto(-350, 0)
ai_paddle.shapesize(stretch_wid=6, stretch_len=0.5)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = random.choice([0.1, -0.1])
ball.dy = random.choice([0.1, -0.1])

# Function to calculate dy based on dx and launch angle
def calculate_dy(dx, launch_angle):
    launch_angle_rad = math.radians(launch_angle)
    dy = dx * math.tan(launch_angle_rad)
    speed_factor = 0.2  # Adjust as needed
    return dy * speed_factor

# Panel
panel = turtle.Turtle()
panel.speed(0)
panel.color('green')
panel.penup()
panel.hideturtle()
panel.goto(0, 260)
panel.write('AI: 0 - 0 :Player', align='center', font=('Courier', 26, 'normal'))

# Paddle Movement
def player_paddle_up():
    y = player_paddle.ycor()
    y += 20
    player_paddle.sety(y)

def player_paddle_down():
    y = player_paddle.ycor()
    y -= 20
    player_paddle.sety(y)

# Keyboard Binding
window.listen()
window.onkeypress(player_paddle_up, 'Up')
window.onkeypress(player_paddle_down, 'Down')

# Update AI Paddle
def update_ai_paddle():
    if ball.ycor() > ai_paddle.ycor():
        ai_paddle.sety(ai_paddle.ycor() + 2)  # Adjust the AI's speed as needed
    elif ball.ycor() < ai_paddle.ycor():
        ai_paddle.sety(ai_paddle.ycor() - 2)  # Adjust the AI's speed as needed

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
        player_score += 1
        panel.clear()
        panel.write('AI: {} - {} :Player'.format(player_score, ai_score), align='center', font=('Courier', 24, 'normal'))

        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -390:
        ai_score += 1
        panel.clear()
        panel.write('AI: {} - {} :Player'.format(player_score, ai_score), align='center', font=('Courier', 24, 'normal'))

        ball.goto(0, 0)
        ball.dx *= -1

    # Ball hitting paddles
    if (340 > ball.xcor() > 330) and (player_paddle.ycor() + 50 > ball.ycor() > player_paddle.ycor() - 50):
        ball.color('red')
        ball.setx(330)
        ball.dx *= -1
    elif (-340 < ball.xcor() < -330) and (ai_paddle.ycor() + 50 > ball.ycor() > ai_paddle.ycor() - 50):
        ball.color('white')
        ball.setx(-330)
        ball.dx *= -1

    # Update AI Paddle
    update_ai_paddle()
