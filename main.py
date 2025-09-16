from pathlib import Path
import typer

from core.board import Map, Cell, Digit
from core.loader import load

app = typer.run


def main():
    resolved_map = Map.create(load(Path("examples/1-resolved.txt")))
    # unresolved_map = Map.create(load(Path("examples/1-unresolved.txt")))
    # empty_map = Map.create(load(Path("examples/1-empty.txt")))

    # print(resolved_map)
    print(resolved_map.get_boxes())


if __name__ == "__main__":
    main()