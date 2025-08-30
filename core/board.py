

class Digit:
    """
    Represents a single digit
    """
    def __init__(
        self, 
        digit: int
        ):
        if 1 <= digit <= 9:
            self.digit = digit
        else:
            raise Exception("Digit must be in range: 1 <= x <= 9")
    
    def __repr__(self):
        return f"Digit({self.digit})"
    
    def __str__(self):
        return f"{self.digit}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Digit):
            if self.digit == other.digit:
                return True
        if isinstance(other, int):
            if self.digit == other:
                return True
        return False
    
    def __ne__(self, other) -> bool:
        if isinstance(other, Digit):
            if self.digit == other.digit:
                return False
        if isinstance(other, int):
            if self.digit == other:
                return False
        return True
    
    def __int__(self):
        return self.digit
    
    
class Cell:
    """
    Represents one cell in a sudoku as a list of possible digits
    """
    def __init__(
        self, 
        digit: Digit | list[Digit] | None = None
        ):
        if digit:
            if type(digit) is Digit:
                self.possibilities = [digit]
            elif type(digit) is list[Digit]:
                self.possibilities = digit
            else:
                TypeError("Must be of type Digit or list[Digit]")
        else:
            self.possibilities = [Digit(1), Digit(2), Digit(3), Digit(4), Digit(5), Digit(6), Digit(7), Digit(8), Digit(9)]
    
    def __repr__(self):
        return f"Cell({self.possibilities})"
    
    def __str__(self):
        return f"{self.possibilities}"
    
    def __contains__(self, digit: Digit | int):
        if digit in self.possibilities:
            return True
        return False        
    
    def __sub__(self, digit: Digit | int):
        if type(digit) is Digit:
            self.possibilities.remove(digit)
        elif type(digit) is int:
            self.possibilities.remove(Digit(digit))
        else:
            TypeError("Must be a type of Digit or int")
        return self.possibilities


class Map:
    """
    Stores sudoku data in a flat list[]. Each value is a list of possibilities that can occur in a cell. Oncea Cell reaches one possibility it is set
    """
    def __init__(
        self, 
        cells: list[int] | list[Cell] = [Cell()] * 81,
        # cells_array: list[list[Cell]] = [[Cell()]*9]*9 
        ):
        self.cells = cells
        # self.cells_array = cells_array
        # self.cells = list(map(lambda a: Cell(a), cells))
        
    def __repr__(self):
        return f"Map({self.cells})"
    
    def __str__(self):
        return f"{self.cells}"
    
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
    