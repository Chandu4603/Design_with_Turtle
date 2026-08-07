import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Lord Jagannath Drawing")
screen.setup(width=800, height=800)

t = turtle.Turtle()
t.speed(0)  # Instant drawing speed
t.pensize(2)
t.hideturtle()

# Helper function to move without drawing
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Function to draw a filled circle
def draw_circle(x, y, radius, color, outline_color=None):
    move(x, y - radius)  # Start from bottom of circle
    if outline_color:
        t.pencolor(outline_color)
    else:
        t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a simplified ellipse for the feather
def draw_feather_shape(x, y, radius_x, radius_y, color):
    t.penup()
    t.goto(x, y - radius_y)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(45)
    t.circle(radius_x * 1.5, 90)
    t.left(90)
    t.circle(radius_x * 1.5, 90)
    t.setheading(0)
    t.end_fill()

# Function to draw the Tilak (U shape)
def draw_tilak(x, y):
    move(x - 15, y)
    t.pencolor("#E6B800") # Golden yellow
    t.pensize(5)
    t.setheading(270) # Pointing down
    t.circle(15, 180) # Semi circle
    t.setheading(90)
    t.forward(50) # Left line up
    
    move(x + 15, y)
    t.setheading(270)
    t.setheading(90)
    t.forward(50) # Right line up
    
    # Bottom point of U
    move(x, y - 10)
    t.pensize(3)
    t.dot(10, "#E6B800")
    t.pensize(2)

# Main Drawing code

# --- 1. Right Eye ---
draw_circle(100, 50, 70, "white", "red")
draw_circle(100, 50, 30, "black")

# --- 2. Left Eye ---
draw_circle(-100, 50, 70, "white", "red")
draw_circle(-100, 50, 30, "black")

# --- 3. Tilak ---
draw_tilak(0, 100)

# --- 4. Bigger Smile/Mouth ---
move(-100, -50)         # Moved starting position wider
t.pencolor("red")
t.pensize(18)           # Made slightly thicker for vibrancy
t.setheading(315)       # Adjusted angle for a wider sweep
t.circle(140, 90)       # Increased arc angle to 90 degrees for a bigger smile
t.pensize(2)

# --- 5. Nose Ring/Jewel ---
move(-25, -20)
t.pencolor("white")
t.dot(30, "white")
t.pencolor("black")
t.dot(25, "black")
t.pencolor("white")
t.dot(22, "white")
t.pencolor("black")
t.dot(19, "black")
t.dot(12, "red")

# --- 6. Peacock Feather ---
feather_base_x = 120
feather_base_y = 200

t.setheading(0)
draw_feather_shape(feather_base_x, feather_base_y, 40, 60, "green")
draw_feather_shape(feather_base_x, feather_base_y - 5, 30, 45, "blue")
draw_feather_shape(feather_base_x, feather_base_y - 10, 15, 25, "purple")

t.pensize(1)
t.pencolor("green")
for angle in range(-20, 21, 5):
    move(feather_base_x, feather_base_y - 30)
    t.setheading(60 + angle)
    t.forward(70)

# Done
screen.update()
turtle.done()