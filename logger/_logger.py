from logger._level import Level
from logger._color import ConsoleColors
from logger._config import Config
from engine.arguments.parser import parse_args
import os
class __Logger():
    
    __name: str
    __level: Level
    __filepath: str = ""
    
    def __init__(self):
        
        args = parse_args()
        Config.set_config_from_dict(args)
        self.__name = Config.get_log_name()
        self.__level = Config.get_log_level()
        filepath = Config.get_log_file()
        if filepath:
            self.__filepath = os.path.abspath(filepath)
            os.makedirs(os.path.dirname(self.__filepath), exist_ok=True)

    def _log(self, level: Level, message: str | Exception, color: ConsoleColors):
        if self.__level <= level:
            if self.__filepath:
                with open(self.__filepath, 'a') as file:
                    file.write(f"[{level}] [{self.__name}] {message}\n")

            print(f"[{color}{level}{ConsoleColors.RESET}] [{ConsoleColors.PURPLE}{self.__name}{ConsoleColors.RESET}] {message}")