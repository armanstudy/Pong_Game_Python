from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0  # Right paddle score
        self.score2 = 0  # Left paddle score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear and update the scoreboard display."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.score2, align="center", font=("Courier", 80, "normal"))  # Left paddle score
        self.goto(100, 200)
        self.write(self.score1, align="center", font=("Courier", 80, "normal"))  # Right paddle score

    def right_score(self):
        """Increment the right paddle's score."""
        self.score1 += 1
        self.update_scoreboard()

    def left_score(self):
        """Increment the left paddle's score."""
        self.score2 += 1
        self.update_scoreboard()