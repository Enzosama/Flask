from typing import Any

class Filter:
    source: Any
    def __init__(self, source) -> None: ...
    def __iter__(self): ...
    def __getattr__(self, name: str): ...
