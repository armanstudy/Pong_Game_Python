from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.tracer(0)  # Disable automatic screen updates for better performance

# Create paddles
paddle1 = Paddle((350, 0))  # Right paddle
paddle2 = Paddle((-350, 0))  # Left paddle

# Create scoreboard
scoreboard = Scoreboard()

# Set up paddle controls
screen.listen()
screen.onkey(paddle1.move_up, "Up")  # Right paddle up
screen.onkey(paddle1.move_down, "Down")  # Right paddle down
screen.onkey(paddle2.move_up, "w")  # Left paddle up
screen.onkey(paddle2.move_down, "s")  # Left paddle down

# Create the ball
ball = Ball()

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control ball speed
    screen.update()  # Refresh the screen
    ball.move()  # Move the ball

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collide()

    # Detect collision with paddles
    if (ball.xcor() > 320 and ball.distance(paddle1) < 50) or (ball.xcor() < -320 and ball.distance(paddle2) < 50):
        ball.paddle_collide()

    # Detect when paddles miss the ball and update the score
    if ball.xcor() > 380:
        ball.ball_position_reset()
        scoreboard.left_score()  # Left paddle scores
    if ball.xcor() < -380:
        ball.ball_position_reset()
        scoreboard.right_score()  # Right paddle scores

screen.exitonclick()