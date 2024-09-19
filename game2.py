import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Catch the Falling Objects")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic animation

# Score and Lives
score = 0
lives = 3

# Pen for score and lives
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("black")
pen.goto(0, 260)
pen.write(f"Score: {score}  Lives: {lives}", align="center", font=("Courier", 24, "normal"))

# Player (Basket)
basket = turtle.Turtle()
basket.shape("square")
basket.color("brown")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)

# Falling Objects
num_objects = 5
objects = []

for _ in range(num_objects):
    obj = turtle.Turtle()
    obj.shape("circle")
    obj.color("red")
    obj.penup()
    obj.speed(0)
    obj.goto(random.randint(-280, 280), random.randint(300, 400))
    obj.dy = random.uniform(2, 5)  # Falling speed
    objects.append(obj)

# Player movement
basket_speed = 20

def move_left():
    x = basket.xcor()
    x -= basket_speed
    if x < -280:
        x = -280
    basket.setx(x)

def move_right():
    x = basket.xcor()
    x += basket_speed
    if x > 280:
        x = 280
    basket.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Function to update score and lives display
def update_display():
    pen.clear()
    pen.write(f"Score: {score}  Lives: {lives}", align="center", font=("Courier", 24, "normal"))

# Main game loop
game_over = False
while not game_over:
    screen.update()

    for obj in objects:
        # Move the object down
        y = obj.ycor()
        y -= obj.dy
        obj.sety(y)

        # Check if object is caught
        if obj.distance(basket) < 50 and obj.ycor() < -240:
            score += 1
            update_display()
            # Reset the object to top
            obj.goto(random.randint(-280, 280), random.randint(300, 400))
            obj.dy = random.uniform(2, 5)

        # Check if object missed
        if obj.ycor() < -300:
            lives -= 1
            update_display()
            # Reset the object to top
            obj.goto(random.randint(-280, 280), random.randint(300, 400))
            obj.dy = random.uniform(2, 5)

            if lives == 0:
                game_over = True
                break

    time.sleep(0.017)  # Approximately 60 frames per second

# Display Game Over
pen.goto(0, 0)
pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
pen.goto(0, -40)
pen.write(f"Final Score: {score}", align="center", font=("Courier", 24, "normal"))

# Keep the window open until closed by the user
screen.mainloop()
