import turtle
import random

# Create a screen
screen = turtle.Screen()
screen.title("Escape the Maze Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()

# Create the exit (goal) at random position
exit = turtle.Turtle()
exit.shape("square")
exit.color("green")
exit.penup()
exit.goto(random.randint(-200, 200), random.randint(-200, 200))

# Create walls of the maze
walls = []

def create_wall(x, y, width, height):
    wall = turtle.Turtle()
    wall.shape("square")
    wall.color("red")
    wall.shapesize(stretch_wid=height, stretch_len=width)
    wall.penup()
    wall.goto(x, y)
    walls.append(wall)

# Create random walls
for _ in range(8):
    x, y = random.randint(-250, 250), random.randint(-250, 250)
    width, height = random.randint(1, 3), random.randint(1, 3)
    create_wall(x, y, width, height)

# Player movement
def go_up():
    player.setheading(90)
    player.forward(20)

def go_down():
    player.setheading(270)
    player.forward(20)

def go_left():
    player.setheading(180)
    player.forward(20)

def go_right():
    player.setheading(0)
    player.forward(20)

# Check for collision with walls
def is_collision_with_wall():
    for wall in walls:
        if player.distance(wall) < 20:
            return True
    return False

# Check if player reached the exit
def check_exit():
    if player.distance(exit) < 20:
        player.goto(0, 0)
        print("You won! Restarting the game...")
        exit.goto(random.randint(-200, 200), random.randint(-200, 200))
        reset_walls()

# Reset walls to random positions
def reset_walls():
    for wall in walls:
        wall.goto(random.randint(-250, 250), random.randint(-250, 250))

# Game loop to check collisions and win conditions
def game_loop():
    if is_collision_with_wall():
        print("Hit the wall! Restarting the game...")
        player.goto(0, 0)  # Reset player position
    check_exit()
    screen.ontimer(game_loop, 100)  # Run this loop every 100ms

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Start the game loop
game_loop()

screen.mainloop()
