from matplotlib import pyplot as plt
import math

a = 1
b = 1

coordinates = [
    (0, 0),
    (2 * a, 0),
    (a, b),
    (1.5 * a, b / 2)
]


lines = [(0, 0, 2 * a, 0), (0, 0, a, b), (a, b, 2 * a, 0)]

for line in lines:
    # (x1, y1, x2, y2) = line
    plt.axline((line[0], line[1]), (line[2], line[3]))

plt.scatter(*zip(*coordinates))
plt.show()