from itertools import chain
from click import FileError
from typer import FileText, FileTextWrite, Exit
from rich import print



def load(file: FileText) -> list[int]:
    try:
        data = file.read()
        return list(map(int, filter(str.isdigit, chain.from_iterable(data))))
    except OSError as e:
        print(f"[red]Failed to load the map: {e}[/red]")
        raise Exit(code=2)
    except FileError as e:
        print(f"[red]Failed to load the map: {e}[/red]")
        raise Exit(code=2)

def save(file: FileTextWrite, data: str):
    try:
        rows = data.split('\n')
        for row in rows:
            file.write(row)
            file.write('\n')
    except OSError as e:
        print(f"[red]Failed to save the map: {e}[/red]")
        raise Exit(code=2)
    except FileError as e:
        print(f"[red]Failed to save the map: {e}[/red]")
        raise Exit(code=2)
