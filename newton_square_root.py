# Approximate the square root of x using Newton's method.

x = 7
g = 1
c = 0

while abs(g*g - x) >= 0.1:
    g = (g + x/g) / 2
    c = c + 1

print(f"The square root of {x} is approximately {g}, found after {c} iterations.")