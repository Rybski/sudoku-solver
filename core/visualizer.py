from core.board import Map, Cell, Digit
from rich.table import Table
from rich import box



def build_cell(map: Map, cell_index: int) -> str:
    return f"{(1 in map.get_cell_by_index(cell_index))*1} {(2 in map.get_cell_by_index(cell_index))*2} {(3 in map.get_cell_by_index(cell_index))*3}\n{(4 in map.get_cell_by_index(cell_index))*4} {(5 in map.get_cell_by_index(cell_index))*5} {(6 in map.get_cell_by_index(cell_index))*6}\n{(7 in map.get_cell_by_index(cell_index))*7} {(8 in map.get_cell_by_index(cell_index))*8} {(9 in map.get_cell_by_index(cell_index))*9}"

def build_visualization(label: str, map: Map, changes = None) -> Table:
    grid = Table(title=label, expand=False, padding=0, show_header=False, show_lines=True, box=box.HEAVY_EDGE)
    grid.add_column(justify="center", vertical="middle", min_width=5, max_width=15, ratio=1, no_wrap=True)
    grid.add_column(justify="center", vertical="middle", min_width=5, max_width=15, ratio=1, no_wrap=True)
    grid.add_column(justify="center", vertical="middle", min_width=5, max_width=15, ratio=1, no_wrap=True)
    grid.add_column(justify="center", vertical="middle", min_width=5, max_width=15, ratio=1, no_wrap=True)
    grid.add_column(justify="center", vertical="middle", min_width=5, max_width=15, ratio=1, no_wrap=True)
    grid.add_column(justify="center", vertical="middle", min_width=5, max_width=15, ratio=1, no_wrap=True)
    grid.add_column(justify="center", vertical="middle", min_width=5, max_width=15, ratio=1, no_wrap=True)
    grid.add_column(justify="center", vertical="middle", min_width=5, max_width=15, ratio=1, no_wrap=True)
    grid.add_column(justify="center", vertical="middle", min_width=5, max_width=15, ratio=1, no_wrap=True)
    grid.add_row(build_cell(map, 0), build_cell(map, 1), build_cell(map, 2), build_cell(map, 3), build_cell(map, 4), build_cell(map, 5), build_cell(map, 6), build_cell(map, 7), build_cell(map, 8))
    grid.add_row(build_cell(map, 9), build_cell(map, 10), build_cell(map, 11), build_cell(map, 12), build_cell(map, 13), build_cell(map, 14), build_cell(map, 15), build_cell(map, 16), build_cell(map, 17))
    grid.add_row(build_cell(map, 18), build_cell(map, 19), build_cell(map, 20), build_cell(map, 21), build_cell(map, 22), build_cell(map, 23), build_cell(map, 24), build_cell(map, 25), build_cell(map, 26))
    grid.add_row(build_cell(map, 27), build_cell(map, 28), build_cell(map, 29), build_cell(map, 30), build_cell(map, 31), build_cell(map, 32), build_cell(map, 33), build_cell(map, 34), build_cell(map, 35))
    grid.add_row(build_cell(map, 36), build_cell(map, 37), build_cell(map, 38), build_cell(map, 39), build_cell(map, 40), build_cell(map, 41), build_cell(map, 42), build_cell(map, 43), build_cell(map, 44))
    grid.add_row(build_cell(map, 45), build_cell(map, 46), build_cell(map, 47), build_cell(map, 48), build_cell(map, 49), build_cell(map, 50), build_cell(map, 51), build_cell(map, 52), build_cell(map, 53))
    grid.add_row(build_cell(map, 54), build_cell(map, 55), build_cell(map, 56), build_cell(map, 57), build_cell(map, 58), build_cell(map, 59), build_cell(map, 60), build_cell(map, 61), build_cell(map, 62))
    grid.add_row(build_cell(map, 63), build_cell(map, 64), build_cell(map, 65), build_cell(map, 66), build_cell(map, 67), build_cell(map, 68), build_cell(map, 69), build_cell(map, 70), build_cell(map, 71))
    grid.add_row(build_cell(map, 72), build_cell(map, 73), build_cell(map, 74), build_cell(map, 75), build_cell(map, 76), build_cell(map, 77), build_cell(map, 78), build_cell(map, 79), build_cell(map, 80))
    return grid


    