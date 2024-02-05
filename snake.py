from turtle import Turtle


STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
#MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creates a snake at a starting position
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Moves snake by forward
    def move(self, difficulty):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(difficulty)

    # Changes direction of the snake up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Changes direction of the snake down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Changes direction of the snake right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Changes direction of the snake left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # When snake eats food add another segment to the end
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("pink")
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Extends the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())


