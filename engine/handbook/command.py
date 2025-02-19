from dataclasses import dataclass

@dataclass
class Command:
    name: str
    function: callable

