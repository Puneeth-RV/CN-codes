import copy
inf = 999

n = int(input("Enter the number of nodes: "))

cost = []
for i in range(n):
    row = []
    strow = input().split()
    for num in strow:
        row.append(int(num))
    cost.append(row)

distance = copy.deepcopy(cost)

nexthop = []
for i in range(n):
    row = []
    for j in range(n):
        if cost[i][j] != inf and i != j:
            row.append(j)
        else:
            row.append(-1)
    nexthop.append(row)

updated = True
while updated:
    updated = False
    for i in range(n):
        for k in range(n):
            if cost[i][k] != inf:
                for j in range(n):
                    if distance[i][j] > cost[i][k] + distance[k][j]:
                        distance[i][j] = cost[i][k] + distance[k][j]
                        nexthop[i][j] = k
                        updated = True

for i in range(n):
    print("\nTable of", i)
    print("Destination\tCost\tNext hop")
    for j in range(n):
        if i != j:
            print(f"{j}\t\t{distance[i][j]}\t{nexthop[i][j]}")
