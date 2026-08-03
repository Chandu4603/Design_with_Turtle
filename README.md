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

## 🚀 Getting Started

### Prerequisites

* **Python 3.x** installed on your system.
* The `turtle`, `math`, and `random` modules (included in the Python standard library, no extra `pip install` required).
