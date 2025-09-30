from core.board import Map

def is_empty(sudoku_map: Map) -> bool:
    if not all(map(lambda _: check_empty(_), sudoku_map.get_rows())):
        return False
    if not all(map(lambda _: check_empty(_), sudoku_map.get_columns())):
        return False
    if not all(map(lambda _: check_empty(_), sudoku_map.get_boxes())):
        return False
    return True

def is_valid(sudoku_map: Map) -> bool:
    if not all(map(lambda _: check_unique(_), sudoku_map.get_rows())):
        return False
    if not all(map(lambda _: check_unique(_), sudoku_map.get_columns())):
        return False
    if not all(map(lambda _: check_unique(_), sudoku_map.get_boxes())):
        return False
    return True

def is_solved(sudoku_map: Map) -> bool:
    if not is_valid(sudoku_map):
        return False
    if not all(map(lambda _: check_set(_), sudoku_map.get_rows())):
        return False
    if not all(map(lambda _: check_set(_), sudoku_map.get_columns())):
        return False
    if not all(map(lambda _: check_set(_), sudoku_map.get_boxes())):
        return False
    return True
        
def check_set(cells: list) -> bool:
    if not all(cells):
        return False
    if not all(map(lambda _: len(_) == 1, cells)):
        return False
    return True

def check_unique(cells: list) -> bool:
    seen_values: set = set()
    empty_cells: int = 0
    for each in cells:
        if len(each) == 1:
            seen_values.update(each)
        else:
            empty_cells += 1
    if len(seen_values)+empty_cells != 9:
        return False
    return True

def check_empty(cells: list) -> bool:
    if not all(map(lambda _: len(_) == 9, cells)):
        return False
    return True