from itertools import chain
from pathlib import Path


def load(filepath: str) -> list[int]:
    with open(Path(filepath), "r") as file:
        return list(map(int, filter(str.isdigit, chain.from_iterable(file))))

def save(filepath: str, data: str):
    with open(Path(filepath), 'w') as f:
        rows = data.split('\n')
        for row in rows:
            f.write(row)
            f.write('\n')