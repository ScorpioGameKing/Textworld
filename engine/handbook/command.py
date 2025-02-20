from dataclasses import dataclass

@dataclass
class Command:
    name: str
    function: callable

    def __hash__(self):
        return f"{self.name} {self.function}".__hash__()
    
    def __getstate__(self):
        return (self.name, self.function)
    
    def __setstate__(self, state):
        (self.name, self.function) = state