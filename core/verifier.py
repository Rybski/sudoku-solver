from core.board import Map

def verify(map: Map) -> bool:
    if not check_rows(map):
        return False
    if not check_columns(map):
        return False
    if not check_boxes(map):
        return False
    return True
    
def check_rows(map: Map) -> bool:
    for row in map.get_rows():
        if not check_set(row):
            return False
        if not check_unique(row):
            return False
    return True

def check_columns(map: Map) -> bool:
    for row in map.get_columns():
        if not check_set(row):
            return False
        if not check_unique(row):
            return False
    return True

def check_boxes(map: Map) -> bool:
    for row in map.get_boxes():
        if not check_set(row):
            return False
        if not check_unique(row):
            return False
    return True
        
def check_set(cells: list) -> bool:
    if not all(cells):
        return False
    if not all(map(lambda _: len(_) == 1, cells)):
        return False
    return True

def check_unique(cells: list) -> bool:
    if not len(set(map(lambda _: list(_)[0], cells))) == 9:
        return False
    return True