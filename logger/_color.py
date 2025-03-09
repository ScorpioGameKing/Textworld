from enum import Enum


class ConsoleColors(Enum):
    
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    CRITICAL = '\033[1;31m'
    RESET = '\033[0m'
    
    def __str__(self):
        return self.value
    
    def __add__(self, other):
        return self.value + other.__str__()