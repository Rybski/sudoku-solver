
from typing import Iterable


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
    Represents one cell in a sudoku as a list of possible digits
    """
    def __init__(
        self, 
        digits: Iterable[Digit]
        ):
        super().__init__(digits)
    
    @classmethod
    def create(cls, digits = None):
        if(isinstance(digits, type(None))):
            return cls({Digit(1), Digit(2), Digit(3), Digit(4), Digit(5), Digit(6), Digit(7), Digit(8), Digit(9)})

        if(isinstance(digits, int)):
            return cls({Digit(digits)})

        if(isinstance(digits, (list, set, tuple))):
            if all(isinstance(_, int) for _ in digits):
                return cls(set(map(lambda _: Digit(_), digits)))

        raise Exception("Invalid type") 

    def __repr__(self):
        return f"Cell({sorted(self)})"

    def __str__(self):
        return f"{sorted(self)}"

    def remove(self, digit: int):
        self.discard(Digit(digit))


class Map:
    """
    Stores sudoku data in a flat list[]. Each value is a list of possibilities that can occur in a cell. Oncea Cell reaches one possibility it is set
    """
    def __init__(
        self, 
        cells: list[int] | list[Cell] = [Cell()] * 81,
        ):
        self.cells = cells
            
    @classmethod
    def create(cls, data):
        if isinstance(data, type(None)):
            return cls() # return a list filled with empty Cells
        
        if isinstance(data, (tuple, set, list)):
            if all(isinstance(_, int) for _ in data):
                return cls() # return a list of Cells
            
        raise Exception("Invalid type") 


    def __repr__(self) -> str:
        return f"Map({self.cells})"
    
    def __str__(self) -> str:
        _ = ''
        for row in self.get_rows():
            _ += f"{row}\n"
        return _
    
    def get_collumns(self) -> list[Cell]:
        columns = []
        for i in range(0,9):
            columns.append(self.cells[i:80:9])
        return columns
    
    def get_rows(self) -> list[Cell]:
        rows = []
        for i in range(0,9):
            rows.append(self.cells[i*9:(i+1)*9:1])
        return rows
    
    def get_collumn(self, index: Digit):
        return self.cells[index:80:9]
    
    def get_row(self, index: Digit):
        return self.cells[int(index)*9:(int(index)+1)*9:1]
    