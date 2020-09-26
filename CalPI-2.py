from time import perf_counter
from random import random
darts = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(1, darts + 1):
    x, y = random(), random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / darts)
print(f"圆周率是：{pi}")
print("运行时间是：{:.5f}s".format(perf_counter() - start))
