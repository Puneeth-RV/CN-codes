INF = 999
n = int(input("Enter number of nodes: "))

print("Enter adjacency matrix (use 999 for no direct link):")
cost = []

for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

distance = [[cost[i][j] for j in range(n)] for i in range(n)]
next_hop = [[j if cost[i][j] != INF and i != j else -1 for j in range(n)] for i in range(n)]

updated = True
while updated:
    updated = False
    for i in range(n):
        for k in range(n):
            if cost[i][k] != INF:
                for j in range(n):
                    if distance[i][j] > cost[i][k] + distance[k][j]:
                        distance[i][j] = cost[i][k] + distance[k][j]
                        next_hop[i][j] = k
                        updated = True

for i in range(n):
    print(f"\nRouting Table for Node {i}:")
    print("Destination\tCost\tNext Hop")
    for j in range(n):
        if i != j:
            print(f"{j}\t\t{distance[i][j]}\t{next_hop[i][j]}")


            
