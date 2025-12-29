expected = 0
total_frames = 20
window_size = 5  

print("Go-Back-N ARQ Receiver\n")

for _ in range(total_frames):
    frame = int(input("Enter received frame: "))

    if frame == expected:
        print(f"Frame {frame} accepted. ACK {frame} sent.")
        expected += 1
    else:
        print(f"Frame {frame} discarded.")
        print(f"ACK {expected - 1} sent.")
        print(f"Sender retransmits frames {expected} to {expected + window_size - 1}\n")
