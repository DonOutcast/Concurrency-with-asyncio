import sys

[sys.stdout.buffer.write(b'Hello!!\n') for _ in range(1_000_000)]

sys.stdout.flush()
