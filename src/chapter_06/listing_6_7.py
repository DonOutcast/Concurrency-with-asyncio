import time

freqs = {}

with open("googlebooks-eng-all-1gram-20120701-a", "r", encoding="utf-8") as f:
    lines = f.readlines()

    start = time.time()

    for line in lines:
        data = line.split('\t')
        word = data[0]
        count = int(data[2])
        if word in freqs:
            freqs[word] = freqs[word]
        else:
            freqs[word] = count
    end = time.time()
    print(f"{end - start}")

