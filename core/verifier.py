from core.board import Map

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
    if False:
        return False
    return True

def check_unique_old(cells: list) -> bool:
    if not len(set(map(lambda _: list(_)[0], cells))) == 9:
        return False
    return True