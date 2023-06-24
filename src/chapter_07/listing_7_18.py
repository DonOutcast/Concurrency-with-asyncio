import time
import numpy as np

data_points = 4_000_000_000
rows = 50
columns = int(data_points / rows)

matrix = np.arange(data_points).reshape(rows, columns)

start = time.time()

res = np.mean(matrix, axis=1)

end = time.time()
print(end - start)
