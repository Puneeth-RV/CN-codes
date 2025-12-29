expected = 0

print("Stop-and-Wait ARQ Receiver (0/1 Sequence Numbers)\n")

for _ in range(20):
    frame = int(input("Enter received frame (0 or 1): "))

    if frame == expected:
        print(f"Frame {frame} received. ACK {frame} sent.")
        expected = 1 - expected   
    else:
        print(f"Frame {frame} discarded. ACK {1 - expected} resent.")


