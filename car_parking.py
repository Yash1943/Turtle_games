import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Car Parking Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create car (player turtle)
car = turtle.Turtle()
car.shape("square")
car.color("blue")
car.shapesize(stretch_wid=1, stretch_len=2)
car.penup()
car.goto(random.randint(-250, 250), random.randint(-250, 250))
car.speed(0)

# Create the parking spot
parking_spot = turtle.Turtle()
parking_spot.shape("square")
parking_spot.color("green")
parking_spot.shapesize(stretch_wid=2, stretch_len=3)
parking_spot.penup()
parking_spot.goto(random.randint(-200, 200), random.randint(-200, 200))

# Create the walls
walls = []

def create_wall(x, y, width, height):
    wall = turtle.Turtle()
    wall.shape("square")
    wall.color("red")
    wall.shapesize(stretch_wid=height, stretch_len=width)
    wall.penup()
    wall.goto(x, y)
    walls.append(wall)

# Randomly generate walls
for _ in range(6):
    x, y = random.randint(-250, 250), random.randint(-250, 250)
    width, height = random.randint(1, 3), random.randint(2, 5)
    create_wall(x, y, width, height)

# Player movement (car)
def go_up():
    car.setheading(90)
    car.forward(20)

def go_down():
    car.setheading(270)
    car.forward(20)

def go_left():
    car.setheading(180)
    car.forward(20)

def go_right():
    car.setheading(0)
    car.forward(20)

# Check for collision with walls
def is_collision_with_wall():
    for wall in walls:
        if car.distance(wall) < 20:
            return True
    return False

# Check if car is parked correctly
def check_parking():
    if parking_spot.distance(car) < 20 and car.heading() == 0:  # Fully aligned, facing right (0 degrees)
        return True
    return False

# Reset game if collision or successful parking
def reset_game():
    if is_collision_with_wall():
        print("Crashed into a wall! Restarting the game...")
        car.goto(random.randint(-250, 250), random.randint(-250, 250))
        car.setheading(0)  # Reset orientation

    if check_parking():
        print("Parked Successfully! You won!")
        car.goto(random.randint(-250, 250), random.randint(-250, 250))
        parking_spot.goto(random.randint(-200, 200), random.randint(-200, 200))  # New parking spot

# Main game loop
def game_loop():
    reset_game()
    screen.ontimer(game_loop, 100)  # Check every 100ms

# Keyboard controls
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Start the game loop
game_loop()

screen.mainloop()


# import turtle
# import random

# # Set up the screen
# screen = turtle.Screen()
# screen.title("Car Parking Game")
# screen.bgcolor("black")
# screen.setup(width=600, height=600)

# # Register the car and parking images
# screen.addshape("car.gif")        # Replace with the path to your car gif
# screen.addshape("parking.gif")    # Replace with the path to your parking gif

# # Create car (player turtle) using custom car image
# car = turtle.Turtle()
# car.shape("car.gif")
# car.penup()
# car.goto(random.randint(-250, 250), random.randint(-250, 250))
# car.speed(0)

# # Create the parking spot using custom parking image
# parking_spot = turtle.Turtle()
# parking_spot.shape("parking.gif")
# parking_spot.penup()
# parking_spot.goto(random.randint(-200, 200), random.randint(-200, 200))

# # Create the walls (same as before)
# walls = []

# def create_wall(x, y, width, height):
#     wall = turtle.Turtle()
#     wall.shape("square")
#     wall.color("red")
#     wall.shapesize(stretch_wid=height, stretch_len=width)
#     wall.penup()
#     wall.goto(x, y)
#     walls.append(wall)

# # Randomly generate walls
# for _ in range(6):
#     x, y = random.randint(-250, 250), random.randint(-250, 250)
#     width, height = random.randint(1, 3), random.randint(2, 5)
#     create_wall(x, y, width, height)

# # Player movement (car)
# def go_up():
#     car.setheading(90)
#     car.forward(20)

# def go_down():
#     car.setheading(270)
#     car.forward(20)

# def go_left():
#     car.setheading(180)
#     car.forward(20)

# def go_right():
#     car.setheading(0)
#     car.forward(20)

# # Check for collision with walls
# def is_collision_with_wall():
#     for wall in walls:
#         if car.distance(wall) < 20:
#             return True
#     return False

# # Check if car is parked correctly
# def check_parking():
#     if parking_spot.distance(car) < 20 and car.heading() == 0:  # Fully aligned, facing right (0 degrees)
#         return True
#     return False

# # Reset game if collision or successful parking
# def reset_game():
#     if is_collision_with_wall():
#         print("Crashed into a wall! Restarting the game...")
#         car.goto(random.randint(-250, 250), random.randint(-250, 250))
#         car.setheading(0)  # Reset orientation

#     if check_parking():
#         print("Parked Successfully! You won!")
#         car.goto(random.randint(-250, 250), random.randint(-250, 250))
#         parking_spot.goto(random.randint(-200, 200), random.randint(-200, 200))  # New parking spot

# # Main game loop
# def game_loop():
#     reset_game()
#     screen.ontimer(game_loop, 100)  # Check every 100ms

# # Keyboard controls
# screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")
# screen.onkey(go_left, "Left")
# screen.onkey(go_right, "Right")

# # Start the game loop
# game_loop()

# screen.mainloop()
