import time
from pathlib import Path

from core.board import Map
from core.loader import load

def benchmark(func, *args, repeats=10000000):
    start = time.perf_counter()
    for _ in range(repeats):
        func(*args)
    end = time.perf_counter()
    return end - start

# usage
for _ in range(0, 5):
    my_map = Map.create(load(Path("examples/1-resolved.txt")))
    elapsed = benchmark(my_map.get_rows2)
    print(f"Elapsed: {elapsed:.6f} seconds")