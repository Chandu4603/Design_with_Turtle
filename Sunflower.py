import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()

golden_angle = 137.508 * (math.pi / 180)  # Convert degrees to radians
num_seeds = 400

for i in range(num_seeds):
    # Calculate radius and angle using Fermat's Spiral formulas
    r = 12 * math.sqrt(i)
    theta = i * golden_angle
    
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    # Map index to HSV hue for radial color shift
    hue = (i / num_seeds) % 1.0
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    
    t.goto(x, y)
    t.dot(8 + (i / 50), rgb)  # Dots get slightly larger toward the outside

screen.update()
turtle.done()