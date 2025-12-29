original_data = input("Enter data bits: ")
generator = input("Enter generator polynomial: ")

data_with_zeros = original_data + '0' * (len(generator) - 1)

data = list(data_with_zeros)
generator = list(generator)

for i in range(len(data) - len(generator) + 1):
    if data[i] == '1':
        for j in range(len(generator)):
            data[i + j] = '0' if data[i + j] == generator[j] else '1'

crc = ''.join(data[-(len(generator) - 1):])

print("CRC Checksum:", crc)
print("Transmitted Data:", original_data + crc)

received = input("Enter received data: ")
received = list(received)

for i in range(len(received) - len(generator) + 1):
    if received[i] == '1':
        for j in range(len(generator)):
            received[i + j] = '0' if received[i + j] == generator[j] else '1'

if '1' in received[-(len(generator) - 1):]:
    print("Error Detected")
else:
    print("No Error Detected")

