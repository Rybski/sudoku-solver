class a:
    def __init__(
        self,
        number: int
        ):
        self.number = number
    
    

class b:
    def __init__(
        self,
        b: a | int | None
        ):
        if type(b) is a:
            self.b = b
        elif type(b) is int:
            self.b = a(b)
        else:
            b = a(0)
            