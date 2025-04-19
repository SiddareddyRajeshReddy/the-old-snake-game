from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Menu(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.speed(0)
        self.boundary_lines = Turtle()
        self.boundary()
        self.menu_options()

    def menu_options(self):
        self.teleport(0, 40)
        self.write("MENU", False, ALIGN, FONT)

    def boundary(self):
        self.boundary_lines.hideturtle()
        self.boundary_lines.speed(0)
        self.boundary_lines.teleport(-290, -290)
        self.boundary_lines.pencolor("white")
        for _ in range(4):
            self.boundary_lines.forward(580)
            self.boundary_lines.left(90)
