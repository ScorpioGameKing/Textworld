from logger._level import Level
import os

class Config:
    log_level: Level = Level.INFO
    log_file: str = ''
    log_name: str = 'Textworld'
    changed: bool = False

    @staticmethod
    def get_log_level() -> Level:
        Config.changed = True
        return Config.log_level

    @staticmethod
    def set_log_level(level: Level):
        Config.log_level = level

    @staticmethod
    def get_log_file() -> str:
        Config.changed = True
        
        return Config.log_file

    @staticmethod
    def set_log_file(file: str):
        Config.log_file = os.path.abspath(file)

    @staticmethod
    def get_log_name() -> str:
        Config.changed = True
        
        return Config.log_name

    @staticmethod
    def set_log_name(name: str):
        Config.log_name = name
        
    @staticmethod
    def set_config_from_dict(config_dict: dict):
        if 'log_level' in config_dict:
            Config.set_log_level(Level(int(config_dict['log_level'])))
        if 'log_file' in config_dict:
            Config.set_log_file(config_dict['log_file'])
        if 'log_name' in config_dict:
            Config.set_log_name(config_dict['log_name'])