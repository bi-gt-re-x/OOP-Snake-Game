from turtle import Turtle

score = 0

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", 'r') as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.shape('square')
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.clear()
        self.write(f"Score: {score}, High Score: {self.highscore} ", move= False, align = "center", font = ("Pixel", 16, "bold"))

    def reset_game(self):
        global score
        if score > self.highscore:
            self.highscore = score
            with open("data.txt", 'w') as data:
                data.write(f"{self.highscore}")
        score = 0
        self.clear()
        self.write(f"Score: {score} High score: {self.highscore}", move = False, align = "center", font = ("Pixel", 16, "bold"))

    def reset_score(self):
        self.clear()

