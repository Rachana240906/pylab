import numpy as np

N = 10
cartesian = np.random.rand(N, 2) * 100
x, y = cartesian[:, 0], cartesian[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
polar = np.column_stack((r, theta))
print(polar)
