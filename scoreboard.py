from turtle import Turtle
FONT = ("Courier", 18 , "normal")

score = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.goto(-230, 260)
        self.ht()
        self.write(f"Score = {score}", False, align="center", font=FONT)

    def score_edit(self):
        global score
        score += 1
        self.clear()
        self.write(f"Score = {score}", False, align="center", font=FONT)

    def game_over(self):
        game_over_turtle = Turtle()
        game_over_turtle.color("red")
        game_over_turtle.speed("fastest")
        game_over_turtle.penup()
        game_over_turtle.goto(0, 0)
        game_over_turtle.ht()
        game_over_turtle.write(f"You Lose", False, align="center", font=FONT)

