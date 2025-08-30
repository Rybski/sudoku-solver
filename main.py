from pathlib import Path
import typer

from core.board import Map, Cell, Digit
from core.loader import load

app = typer.run


def main():
    my_map = Map(load(Path("examples/1-unresolved.txt")))
    print(my_map)

if __name__ == "__main__":
    main()
    pass