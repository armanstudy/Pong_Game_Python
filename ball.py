from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle") 
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
       
    def move(self):
            self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move) #move the ball to the right and up by 10 pixels


    def collide(self):
       self.y_move *= -1 #reverse the y direction of the ball

    def paddle_collide(self):
        self.x_move *= -1 #reverse the x direction of the ball
        self.move_speed *= 0.9 #increase the speed of the ball by 10%

    def ball_position_reset(self): 
        #reset the ball position to the center of the screen
        self.goto(0, 0)
        self.x_move *= -1  #reverse the x direction of the ball
        self.move_speed = 0.1