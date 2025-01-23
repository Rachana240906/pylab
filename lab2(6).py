import math

points = []

for i in range(10):
    x, y, z = map(int, input("Enter point (x y z): ").split())
    points.append((x, y, z))

nearest_neighbors = []

for i in range(10):
    nearest_point = None
    min_distance = float('inf')
    
    for j in range(10):
        if i != j:
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
            
            if distance < min_distance:
                min_distance = distance
                nearest_point = points[j]
    
    nearest_neighbors.append((points[i], nearest_point))

for point, neighbor in nearest_neighbors:
    print(f"Point {point} has nearest neighbor {neighbor}")
