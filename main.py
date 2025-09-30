from sys import stdout
import typer
from rich import print
from rich.live import Live

from core.board import Map, Cell, Digit
from core.io import load, save
from core.verifier import is_empty, is_valid, is_solved
from core.visualizer import build_visualization
from core.solver import strategies, apply_mutation_mask
from core.staus import Status


# solve 
# - <path> input file
# -o --output <path> output file
# -v --visualize run visualizer
# -d --detail step by step visualization
#TODO -r --recursive indicates that the input file is a dir and output file should be one too. Runs for all files in dir
# -s --silent does not print anything to the stdout
# verify
# # - <path> input file
# -o --output <path> output file
# -r --recursive indicates that the input file is a dir and output file should be one too. Runs for all files in dir
# -s --silent does not print anything to the stdout

app = typer.Typer(help="CLI sudoku solver")

@app.command()
def solve(
    infile: typer.FileText = typer.Argument("-", help="Input file (default: stdin)",), 
    outfile: typer.FileTextWrite = typer.Option("-", "--output", "-o", help="Output file (default: stdout)",),
    visualize: bool = False, 
    detail: bool = False, 
    silent: bool = False,
    ):
    iteration = 0
    if detail:
        visualize = True
    status = Status.UNKNOWN
    
    sudoku_map = Map.create(load(infile)) # Guard about bad paths or invalid files! and gracefully exit
    
    if not is_valid(sudoku_map):
        print("Invalid map")
        raise typer.Exit()
    
    if is_solved(sudoku_map):
        status = Status.SOLVED
    elif is_empty(sudoku_map):
        status = Status.EMPTY
    else:
        status = Status.UNSOLVED
    
    if visualize:
        with Live(build_visualization(f"Map: Unknown\niteration: {iteration}{ ", strategy: None" if detail else "" }", sudoku_map), screen=True) as live:
            input()
            while status is Status.UNSOLVED:
                old_sudoku_map = sudoku_map.clone()
                iteration += 1
                for strategy in strategies:
                    mask = strategy(sudoku_map)
                    sudoku_map = apply_mutation_mask(sudoku_map, mask)
                    if is_solved(sudoku_map):
                        status = Status.SOLVED
                    if sudoku_map.is_identical(old_sudoku_map) and not status:
                        status = Status.STUCK
                    if detail:
                        live.update(build_visualization(f"Map: {status}\niteration: {iteration}, strategy: {strategy.__name__}", sudoku_map))
                        input()
                    if status.is_terminable():
                        break
                if not detail:
                    live.update(build_visualization(f"Map: {status}\niteration: {iteration}", sudoku_map))
                    input()
    else:
        while status is Status.UNSOLVED:
            old_sudoku_map = sudoku_map.clone()
            iteration += 1
            for strategy in strategies:
                mask = strategy(sudoku_map)
                sudoku_map = apply_mutation_mask(sudoku_map, mask)
                if is_solved(sudoku_map):
                    status = Status.SOLVED
                if sudoku_map.is_identical(old_sudoku_map) and not status:
                    status = Status.STUCK
                if status.is_terminable():
                    break
                
    if not silent:
        print(sudoku_map)
    save(outfile, str(sudoku_map)) # Default name to be saved should be build from opened filename and exit status

@app.command()
def  check(
    infile: typer.FileText = typer.Argument("-", help="Input file (default: stdin)",), 
    outfile: typer.FileTextWrite = typer.Option("-", "--output", "-o", help="Output file (default: stdout)",),
    ):
    status = Status.UNKNOWN
    
    sudoku_map = Map.create(load(infile))
    
    if not is_valid(sudoku_map):
        status = Status.INVALID
    elif is_solved(sudoku_map):
        status = Status.SOLVED
    elif is_empty(sudoku_map):
        status = Status.EMPTY
    else:
        status = Status.UNSOLVED
    
    if outfile.name != stdout.name:
        print(f"{status}")
    save(outfile, str(status.get_state()))


if __name__ == "__main__":
    app()