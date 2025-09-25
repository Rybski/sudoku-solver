import time
import typer
from rich import print
from rich.console import Console
from rich.live import Live


from core.board import Map, Cell, Digit
from core.io import load, save
from core.verifier import is_valid, is_solved
from core.visualizer import build_visualization
from core.solver import strategies, apply_mutation_mask

app = typer.run


def main():
    iteration = 0
    sudoku_map = Map.create(load("examples/1-unresolved.txt"))
    if not is_valid(sudoku_map):
        raise Exception("Passed sudoku_map is not valid")
    solved = is_solved(sudoku_map)

    with Live(build_visualization(f"Map: Unknown\niteration: {iteration}, strategy: None", sudoku_map), screen=True) as live:
        while not solved:
            old_sudoku_map = sudoku_map.clone()
            iteration += 1
            input()
            for strategy in strategies:
                mask = strategy(sudoku_map)
                sudoku_map = apply_mutation_mask(sudoku_map, mask)
                live.update(build_visualization(f"Map: Unsolved\niteration: {iteration}, strategy: {strategy.__name__}", sudoku_map))
                input()
            if is_solved(sudoku_map):
                solved = True
                live.update(build_visualization(f"Map: [green]Solved[/green]\nIteration: {iteration}, strategy: None", sudoku_map))
                input()
            if sudoku_map.is_identical(old_sudoku_map) and not solved:
                solved = True
                live.update(build_visualization(f"Map: [red]Stuck[/red]\nIteration: {iteration}, strategy: None", sudoku_map))
                input()
    

    save("temp.txt", str(sudoku_map))


if __name__ == "__main__":
    main()