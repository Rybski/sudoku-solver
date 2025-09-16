from pathlib import Path
import typer

from core.board import Map, Cell, Digit
from core.io import load, save

app = typer.run


def main():
    resolved_map = Map.create(load("examples/1-unresolved.txt"))
    save("temp.txt", str(resolved_map))
    loaded_map = Map.create(load("temp.txt"))
    print(loaded_map)


if __name__ == "__main__":
    main()