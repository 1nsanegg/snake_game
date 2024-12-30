from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.score = 0
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over ", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()