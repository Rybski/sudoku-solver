from itertools import chain
from pathlib import Path
from typer import FileText, FileTextWrite


def load(file: FileText) -> list[int]:
    data = file.read()
    return list(map(int, filter(str.isdigit, chain.from_iterable(data))))

def save(file: FileTextWrite, data: str):
    rows = data.split('\n')
    for row in rows:
        file.write(row)
        file.write('\n')
