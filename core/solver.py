from abc import ABC
from collections import defaultdict
from dataclasses import dataclass
from core.board import Map, Cell, Digit


def build_row_mask(map: Map):
    row_mask: defaultdict[int, set[Cell]] = defaultdict(set)
    
    for cell_index in range(len(map)):
        if map.get_cell_by_index(cell_index).is_set():
            others_indexes = map.get_row_others_indexes(cell_index)
            for others_index in others_indexes:
                row_mask[others_index].update(map[cell_index])
    return row_mask

def build_column_mask(map: Map):
    column_mask: defaultdict[int, set[Cell]] = defaultdict(set)
    
    for cell_index in range(len(map)):
        if map.get_cell_by_index(cell_index).is_set():
            others_indexes = map.get_column_others_indexes(cell_index)
            for others_index in others_indexes:
                column_mask[others_index].update(map[cell_index])
    return column_mask

def build_box_mask(map: Map):
    box_mask: defaultdict[int, set[Cell]] = defaultdict(set)
    
    for cell_index in range(len(map)):
        if map.get_cell_by_index(cell_index).is_set():
            others_indexes = map.get_box_others_indexes(cell_index)
            for others_index in others_indexes:
                box_mask[others_index].update(map[cell_index])
    return box_mask

def apply_mutation_mask(map: Map, mutation_mask: defaultdict[int, set[Cell]]) -> Map:
    new_map = map.clone()
    for cell_index in range(len(new_map)):
        new_map[cell_index].difference_update(mutation_mask.get(cell_index, set()))
    return new_map

strategies = [build_row_mask, build_column_mask, build_box_mask]