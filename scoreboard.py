from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # Updates rendering of the score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Increases score by 1
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # Game over after the snake hits the wall or its tail
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


