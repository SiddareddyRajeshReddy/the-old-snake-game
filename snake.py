from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.snake()
        self.eyes = []
        # self.eye1 = Turtle("circle")
        # self.eye1.color("blue")
        # self.eye2 = Turtle("circle")
        # self.eye2.color("red")
        # self.eye1.shapesize(0.2, 0.2)
        # self.eye2.shapesize(0.2, 0.2)
        self.eye()
        self.head = self.snake_parts[0]

    def snake(self):
        if len(self.snake_parts) == 0:
            new_pos = 0
            for i in range(3):
                new_part = Turtle("circle")
                new_part.color("white")
                # new_part.shapesize(0.5, 0.5)
                new_part.penup()
                self.snake_parts.append(new_part)
                new_part.teleport(x=new_pos, y=0)
                new_pos -= 20
        else:
            new_x = self.snake_parts[-1].xcor()
            new_y = self.snake_parts[-1].ycor()
            new_part = Turtle("circle")
            new_part.color("white")
            # new_part.shapesize(0.5, 0.5)
            new_part.penup()
            self.snake_parts.append(new_part)
            new_part.teleport(new_x, new_y)

    def eye(self):
        self.eyes.append(Turtle("circle"))
        self.eyes.append(Turtle("circle"))
        self.eyes[0].shapesize(0.2, 0.2)
        self.eyes[1].shapesize(0.2, 0.2)
        self.eyes[0].color("black")
        self.eyes[1].color("black")
        self.eyes[0].penup()
        self.eyes[1].penup()
        self.eyes[0].teleport(0, 5)
        self.eyes[1].teleport(0, -5)

    def move(self):
        for i in range(len(self.snake_parts)-1, 0, -1):
            new_x = self.snake_parts[i-1].xcor()
            new_y = self.snake_parts[i-1].ycor()
            self.snake_parts[i].goto(new_x, new_y)
        self.snake_parts[0].fd(MOVE_DISTANCE)
        self.eyes[0].fd(MOVE_DISTANCE)
        self.eyes[1].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.eyes[0].setheading(90)
            self.eyes[1].setheading(90)
            self.eyes[0].teleport(self.head.xcor() - 5, self.head.ycor())
            self.eyes[1].teleport(self.head.xcor() + 5, self.head.ycor())

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.eyes[0].setheading(270)
            self.eyes[1].setheading(270)
            self.eyes[0].teleport(self.head.xcor() + 5, self.head.ycor())
            self.eyes[1].teleport(self.head.xcor() - 5, self.head.ycor())

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.eyes[0].setheading(180)
            self.eyes[1].setheading(180)
            self.eyes[0].teleport(self.head.xcor(), self.head.ycor()-5)
            self.eyes[1].teleport(self.head.xcor(), self.head.ycor()+5)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.eyes[0].setheading(0)
            self.eyes[1].setheading(0)
            self.eyes[0].teleport(self.head.xcor(), self.head.ycor()+5)
            self.eyes[1].teleport(self.head.xcor(), self.head.ycor()-5)

    def restart(self):
        for parts in self.snake_parts:
            parts.color("black")
        self.snake_parts.clear()
        self.snake()
        self.head = self.snake_parts[0]
        for e in self.eyes:
            e.color("black")
        self.eyes = []
        self.eye()