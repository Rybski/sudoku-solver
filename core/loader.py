from itertools import chain
from pathlib import Path


def load(filepath: Path) -> list[int]:
    with open(filepath, "r") as file:
        return list(map(int, filter(str.isdigit, chain.from_iterable(file))))