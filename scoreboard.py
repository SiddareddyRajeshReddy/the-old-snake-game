from turtle import Turtle
FONT = ("Courier", 15, "normal")
AllIGN = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        with open("Highscore.txt") as high:
            self.high_score = int(high.read())
        self.teleport(0, 290)
        self.score = -1
        self.scoreboard()

    def scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High_score: {self.high_score}", False, AllIGN, FONT)

    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.write("Game Over", False, AllIGN, FONT)

    def restart(self):
        if self.score > self.high_score:
            with open("Highscore.txt",mode='w') as high:
                high.write(str(self.score))
                self.high_score = self.score
        self.score = -1
        self.scoreboard()
