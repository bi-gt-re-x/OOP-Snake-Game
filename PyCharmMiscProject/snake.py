from turtle import Screen, Turtle


class Snake:
    def __init__(self):
        self.POS = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for positions in self.POS:
            self.add_segment(positions)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, positions):
        body = Turtle(shape="square")
        body.color("white")
        body.penup()
        body.goto(positions)
        self.segments.append(body)

    def up(self):
        self.segments[0].setheading(90)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)

    def down(self):
        self.segments[0].setheading(270)

    def movers(self):
        self.segments[0].forward(20)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()