window_size = 5
base = 0
received = [False] * 20

print("Selective Repeat ARQ Receiver\n")

for _ in range(20):
    frame = int(input("Enter received frame: "))

    if base <= frame < base + window_size:
        if not received[frame]:
            received[frame] = True
            print(f"Frame {frame} received and ACK sent.")
        else:
            print(f"Duplicate frame {frame} ignored.")

        while base < 20 and received[base]:
            base += 1
    else:
        print(f"Frame {frame} outside window. Ignored.")



