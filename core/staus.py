from enum import IntFlag

META_COLORED_TXT = {
    0: "[gray]UNSOLVED[/gray]",
    1: "[green]SOLVED[/green]",
    2: "[red]STUCK[/red]",
    3: "[red]INVALID[/red]",
    4: "[gray]UNKNOWN[/gray]",
}

META_TXT = {
    0: "UNSOLVED",
    1: "SOLVED",
    2: "STUCK",
    3: "INVALID",
    4: "UNKNOWN",
}

META_TERMINABLE = {
    0: False,
    1: True,
    2: True,
    3: True,
    4: True,
}

class Status(IntFlag):
    UNSOLVED = 0
    SOLVED = 1
    STUCK = 2
    INVALID = 3
    UNKNOWN = 4
    
    def __str__(self) -> str:
        return META_COLORED_TXT.get(self, "[red]BAD STATE[/red]")
    
    def get_state(self) -> str:
        return META_TXT.get(self, "BAD STATE")
    
    def is_terminable(self) -> bool:
        return META_TERMINABLE.get(self, True)
        