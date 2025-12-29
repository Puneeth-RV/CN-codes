n = int(input("Enter number of bit streams (max 5): "))

print("\n1D Parity Check (Even Parity)\n")

for i in range(n):
    data = input(f"Enter 7-bit data stream {i+1}: ")

    ones_count = data.count('1')

    if ones_count % 2 == 0:
        parity_bit = '0'
    else:
        parity_bit = '1'

    transmitted_data = data + parity_bit

    print("Input Data       :", data)
    print("Parity Bit       :", parity_bit)
    print("Transmitted Data :", transmitted_data)
    print()



