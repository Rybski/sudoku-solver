
from typing import Iterable

from core import meta


class Digit(int):
    """
    Represents a single digit
    """
    def __new__(cls, digit):
        if 1 <= digit <= 9:
            return super().__new__(cls, digit)
        raise Exception("digit must be in range 1..9")
    
    def __repr__(self) -> str:
        return f"Digit({int(self)})"
    
    def __str__(self) -> str:
        return str(int(self))


class Cell(set):
    """
    Represents one cell in a sudoku as a list of possible digits. 0 is unresolved
    """
    def __init__(self, digits: Iterable[Digit]):
        super().__init__(digits)
    
    @classmethod
    def create(cls, digits: None | int | list | set | tuple = None):
        if(isinstance(digits, type(None))):
            return cls({Digit(1), Digit(2), Digit(3), Digit(4), Digit(5), Digit(6), Digit(7), Digit(8), Digit(9)})

        if(isinstance(digits, int)):
            if digits == 0: # We might want to store unresolved fields as 0 inside the files...
                return cls({Digit(1), Digit(2), Digit(3), Digit(4), Digit(5), Digit(6), Digit(7), Digit(8), Digit(9)})
            return cls({Digit(digits)})

        if(isinstance(digits, (list, set, tuple))):
            if all(isinstance(_, int) for _ in digits):
                return cls(set(map(lambda _: Digit(_), digits)))

        raise Exception("Invalid type") 

    def __repr__(self):
        if len(self) > 1:
            return f"Cell({0})"
        return f"Cell({list(self)[0]})"

    def __str__(self):
        if len(self) > 1:
            return f"{0}"
        return f"{list(self)[0]}"

    def remove(self, digit: int):
        self.discard(Digit(digit))


class Map(list):
    """
    Stores sudoku data in a flat list[]. Each value is a list of possibilities that can occur in a cell. Oncea Cell reaches one possibility it is set
    """
    def __init__(self, cells: list[Cell]):
        super().__init__(cells)
      
    # 0  1  2  3  4  5  6  7  8
    # 9  10 11 12 13 14 15 16 17
    # 18 19 20 21 22 23 24 25 26
    # 27 28 29 30 31 32 33 34 35
    # 36 37 38 39 40 41 42 43 44
    # 45 46 47 48 49 50 51 52 53
    # 54 55 56 57 58 59 60 61 62
    # 63 64 65 66 67 68 69 70 71
    # 72 73 74 75 76 77 78 79 80
      
    @classmethod
    def create(cls, data: None | list = None):
        if isinstance(data, type(None)):
            return cls([Cell.create() for _ in range(81)]) # return a list filled with empty Cells
        
        if isinstance(data, list):
            if all(isinstance(_, int) for _ in data):
                if len(data) == 81:
                    return cls(list(map(lambda _: Cell.create(_), data))) # coverts all numbers inside the list of values into a cell
                else:
                    raise Exception("Invalid size of the Map")
            
        raise Exception("Invalid type") 


    def __repr__(self) -> str:
        return f"Map({self})"
    
    def __str__(self) -> str:
        _ = ''
        for row in self.get_rows():
            _ += f"{list(map(lambda _: str(_) , row))}\n"
        return _
    
    
    def get_cell_by_index(self, index: int) -> Cell:
        """Get Cell in specific Index

        Args:
            index (int):
            
        Returns:
            cell (Cell): 
        """
        return self[index]
    
    def get_cell(self, row: Digit | int, column: Digit | int) -> Cell:
        """Get Cell in specific Row and Column

        Args:
            row (Digit | int): 
            column (Digit | int): 
            
        Returns:
            cell (Cell): 
        """
        (_, __) = meta.ROW_TO_INDEXES.get(row), meta.COLUMN_TO_INDEXES.get(column)
        if _ is not None and __ is not None:
            index = (set(_) & set(__)).pop()
            return self.get_cell_by_index(index)
        raise Exception("Row or Column out of bounds")

    def get_row_cells(self, row: Digit | int):
        """Get list of items in a row

        Args:
            row (Digit | int):

        Returns:
            items (list):
        """
        indexes = meta.ROW_TO_INDEXES.get(row)
        if indexes is not None:
            return list(map(lambda _: self.get_cell_by_index(_), indexes))
        raise Exception("Row out of bounds")  
    
    def get_rows(self):
        """Get a list of all rows

        Returns:
            rows (list):
        """
        indexes = meta.ROW_TO_INDEXES.values()
        if indexes is not None:
            return list(map(lambda _: list(map(self.get_cell_by_index, _)), indexes))
        raise Exception("Could not get Indexes from Meta tables")
    
    def get_row(self, index):
        """Get a Row of an index

        Args:
            index (int):

        Returns:
            row (list):
        """   
        _ = meta.INDEX_TO_ROW.get(index)
        if _ is not None:
            return _
        raise Exception("index out of bounds")
    
    def get_column_cells(self, column):
        """Get list of items in a column

        Args:
            column (int):

        Returns:
            items (list):
        """
        indexes = meta.COLUMN_TO_INDEXES.get(column)
        if indexes is not None:
            return list(map(lambda _: self.get_cell_by_index(_), indexes))
        raise Exception("Column out of bounds")    
        
    def get_columns(self):
        """Get a list of all columns

        Returns:
            columns (list):
        """
        indexes = meta.COLUMN_TO_INDEXES.values()
        if indexes is not None:
            return list(map(lambda _: list(map(self.get_cell_by_index, _)), indexes))
        raise Exception("Could not get Indexes from Meta tables")
    
    def get_column(self, index):
        """Get a Column of an index

        Args:
            index (int):

        Returns:
            column (list):
        """   
        _ = meta.INDEX_TO_COLUMN.get(index)
        if _ is not None:
            return _
        raise Exception("index out of bounds")

    def get_box_cells(self, box):
        """Get list of items in a box

        Args:
            box (int):

        Returns:
            items (list):
        """
        indexes = meta.BOX_TO_INDEXES.get(box)
        if indexes is not None:
            return list(map(lambda _: self.get_cell_by_index(_), indexes))
        raise Exception("Box out of bounds")    
    
    def get_boxes(self):
        """Get a list of all boxes

        Returns:
            boxes (list):
        """
        indexes = meta.BOX_TO_INDEXES.values()
        if indexes is not None:
            return list(map(lambda _: list(map(self.get_cell_by_index, _)), indexes))
        raise Exception("Could not get Indexes from Meta tables")
    
    def get_box(self, index) -> int:
        """Get a box of an index

        Args:
            index (int):

        Returns:
            box (list):
        """        
        _ = meta.INDEX_TO_BOX.get(index)
        if _ is not None:
            return _
        raise Exception("index out of bounds")
