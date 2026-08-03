# Turtle Projects

# 01. 🎨 Python Turtle Parametric Heart Art

A vibrant Python script using the standard `turtle` graphics library to generate a colorful, geometric heart shape defined by mathematical parametric equations.

---

## 📸 Overview

This program calculates coordinates along a classic parametric heart curve and renders starburst accent lines at each point using randomized rainbow colors against a dark background.

## ✨ Features

* **Mathematical Precision:** Uses heart-shaped parametric equations derived from trigonometric functions ($x(\theta)$ and $y(\theta)$).
* **Dynamic Visuals:** Draws 120 parametric anchor points, each featuring an 8-spoke starburst design.
* **Randomized Palette:** Colors each point dynamically selecting from a 7-color rainbow spectrum (`red`, `orange`, `yellow`, `green`, `blue`, `indigo`, `violet`).
* **Instant Rendering:** Configured with maximum execution speed (`speed(0)`) for fast art generation.

---

## 🧮 How the Math Works

The heart contour is plotted using the following parametric formulas:

$$x = 16 \sin^3(\theta) \times 15$$

$$y = (13 \cos(\theta) - 5 \cos(2\theta) - 2 \cos(3\theta) - \cos(4\theta)) \times 15$$

Where $\theta$ ranges from $0$ to $2\pi$ across 120 steps.

---
## The Final OutPut is Here

<img width="835" height="704" alt="Screenshot 2026-08-04 001721" src="https://github.com/user-attachments/assets/57c2b9db-6c4b-4a9f-8097-0d682cb3dcb0" />
<br>
<center>Heart Art using Python</center>

## 🚀 Getting Started

### Prerequisites

* **Python 3.x** installed on your system.
* The `turtle`, `math`, and `random` modules (included in the Python standard library, no extra `pip install` required).



# 02. 🌻 Mathematical Phyllotaxis (Sunflower Pattern)

An elegant Python script built with `turtle`, `math`, and `colorsys` that models nature's golden ratio spiral—the arrangement of seeds in a sunflower head—using polar coordinates and mathematical equations.

---

## 📸 Visual Overview

 "<img width="903" height="738" alt="Screenshot 2026-08-04 003227" src="https://github.com/user-attachments/assets/111d63a5-3222-42d4-bc0c-a377d67eb069" />"


---

## ✨ Features

* **Natural Optimization:** Simulates real botanical growth patterns observed in sunflowers, pinecones, and succulents.
* **Golden Angle Precision:** Uses trigonometric equations based on the Golden Ratio ($\phi$) to achieve maximum packing density.
* **Dynamic HSV Rainbow Palette:** Colors cycle smoothly across the spectrum using `colorsys.hsv_to_rgb` as seeds expand outward.
* **Instant Turtle Rendering:** Utilizes `screen.tracer(0)` for zero-delay instant graphic generation.

---

## 🧮 How the Math Works

The position of each seed $i$ (where $i = 0, 1, 2, \dots, N$) is calculated in polar coordinates $(r, \theta)$ before being converted into Cartesian $(x, y)$ coordinates for the screen:

### 1. The Golden Angle ($\theta$)
To prevent seeds from aligning in straight rows and leaving empty space, each new seed rotates relative to the previous one by the Golden Angle:

$$\theta = i \times 137.508^\circ$$

### 2. Radius ($r$)
Using Fermat's Spiral equation, the distance from the center grows proportionally to the square root of the index:

$$r = c \sqrt{i}$$

*(where $c$ is a scaling factor controlling spacing)*

### 3. Coordinate Conversion
$$\begin{aligned} x &= r \cos(\theta) \\ y &= r \sin(\theta) \end{aligned}$$

---
### Prerequisites
Python 3.x installed on your system.
The turtle, math, and random modules (included in the Python standard library, no extra pip install required).
