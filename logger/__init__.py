from logger._color import ConsoleColors
from logger._logger import __Logger
from logger._level import Level
from logger._config import Config
from engine.arguments.parser import parse_args


def __init():
    
    if globals().get('logger', None) and not Config.changed:
        return
    
    globals()['logger'] = __Logger()
    
def trace(message: str):
    __init()
    globals()['logger']._log(Level.TRACE, message, color=ConsoleColors.BLUE)
    
def debug(message: str):
    __init()
    globals()['logger']._log(Level.DEBUG, message, color=ConsoleColors.CYAN)

def info(message: str):
    __init()
    globals()['logger']._log(Level.INFO, message, color=ConsoleColors.GREEN)
    
def warning(message: str | Exception):
    __init()
    globals()['logger']._log(Level.WARNING, message, color=ConsoleColors.YELLOW)
    
def error(message: str | Exception):
    __init()
    globals()['logger']._log(Level.ERROR, message, color=ConsoleColors.RED)
    
def critical(message: str | Exception):
    __init()
    globals()['logger']._log(Level.CRITICAL, message, color=ConsoleColors.CRITICAL)
