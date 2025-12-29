import math

n = 10

nodes = {
    0: (10, 20),
    1: (40, 30),
    2: (60, 80),
    3: (90, 20),
    4: (120, 60),
    5: (150, 40),
    6: (180, 90),
    7: (200, 10),
    8: (230, 70),
    9: (260, 50)
}

range_limit = float(input("Enter transmission range: "))
print("\nNeighbour Table:\n")

for i in range(n):
    x1, y1 = nodes[i]
    neighbours = []

    for j in range(n):
        if i != j:
            x2, y2 = nodes[j]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if distance <= range_limit:
                neighbours.append(j)

    print(f"Node {i} neighbours: {neighbours}")








