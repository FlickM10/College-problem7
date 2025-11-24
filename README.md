# 📈 Monte Carlo Simulation: Ellipse Area Estimator

This project uses the **Monte Carlo simulation method** to estimate the area of an ellipse defined by the semi-major axis $a$ and the semi-minor axis $b$.

The Monte Carlo method involves randomly sampling points within a known area (the bounding box) and using the ratio of "successful" hits (points inside the ellipse) to estimate the unknown target area.

## 🎯 Theory & Implementation (Quadrant Simulation)

### Bounding Box

The code simulates the generation of random points in the **first quadrant** of the bounding box, which spans the region $x \in [0, a]$ and $y \in [0, b]$. The area of this smaller bounding region is simply $a \times b$.



### Estimation Formula

The ratio of points inside the ellipse (N_in) to the total points (N) approximates the ratio of the areas in that quadrant:

<img width="263" height="80" alt="image" src="https://github.com/user-attachments/assets/50965876-305b-43c5-ad08-35930d5d64cc" />

Since the true area of the ellipse is $A_{\text{true}} = \pi ab$, we estimate the full area by scaling the simulation results by 4:

$$A_{\text{est}} = 4 \times (a \times b) \times \frac{N_{\text{in}}}{N}$$

---

## 🚀 Getting Started

### Prerequisites

You only need Python installed on your system. This script relies on the built-in `random` and `math` modules.

### Usage

1.  Save the code as a Python file (e.g., `ellipse_mc.py`).
2.  Run the script from your terminal:
    ```bash
    python ellipse_mc.py
    ```
3.  The program will prompt you to enter the values for the semi-major axis (**a**), semi-minor axis (**b**), and the number of random points (**N**).

---

## 📋 Sample Run

Using inputs $a=3$, $b=2$, and $N=100000$:

**Note:** For better accuracy (smaller difference), increase the number of random points (N).
