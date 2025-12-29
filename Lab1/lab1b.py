rows = int(input("Enter number of bit streams (max 5): "))
cols = 7
data = []

for i in range(rows):
    row = input(f"Enter 7-bit data stream {i+1}: ")
    data.append([int(bit) for bit in row])

row_parity = []
for row in data:
    row_parity.append(0 if sum(row) % 2 == 0 else 1)

col_parity = []
for j in range(cols):
    col_sum = sum(data[i][j] for i in range(rows))
    col_parity.append(0 if col_sum % 2 == 0 else 1)

print("\n2D Parity Matrix (Even Parity):")
for i in range(rows):
    print(*data[i], "|", row_parity[i])

print("-" * 20)
print(*col_parity)

