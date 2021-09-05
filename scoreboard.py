from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.setpos(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)