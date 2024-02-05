from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scorebord
#from difficulty import Difficulty
import time

# Constants
EASY = 10
INTERMEDIATE = 15
HARD = 20


def snake_game():

    # Creates screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    # Asks user to choose the difficulty
    difficulty_level = screen.textinput("Choose Difficulty Level",
                                        "Hard, Intermediate or Easy ")
    if difficulty_level.lower() == "hard":
        difficulty = HARD
    elif difficulty_level.lower() == "intermediate":
        difficulty = INTERMEDIATE
    elif difficulty_level.lower() == "easy":
        difficulty = EASY
    else:
        snake_game()

    snake = Snake()
    food = Food()
    scoreboard = Scorebord()

    # Moves the snake in different directions
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Runs the snake game
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move(difficulty)

        # Detects if the snake ate the food
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            food.refresh()
            snake.extend()

        # Detects if snake hit any wall
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            game_on = False
            scoreboard.game_over()

        # Detects if snake hit its own tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()

    # Asks if user wants to continue playing
    user_wants_to_play = screen.textinput("Would you like to continue playing?",
                                          "Press 'y' if you would like to play, anything else otherwise:")
    if user_wants_to_play == "y":
        screen.clear()
        snake_game()
    else:
        screen.exitonclick()


# Initiates the game
snake_game()
