import random
import math

a = float(input("Enter the 'a' side of the ellipse : "))
b = float(input("Enter the 'b' side of the ellipse : "))
A_boundingbox = a * b
N = int(input("Enter the number of random points : "))
N_in = 0

for i in range(N):
    x = random.uniform(0,a)
    y = random.uniform(0,b)
    if (x ** 2 / a ** 2) + (y ** 2 / b ** 2) <= 1:
        N_in = N_in + 1

A_est = 4 * A_boundingbox * N_in / N
print(f"The estimated area of the ellipse is {A_est}")

A_true = math.pi * a * b
print(f"The actual area of ellipse is {A_true}")

Diff = A_true - A_est
print(f"the difference = {Diff}")
