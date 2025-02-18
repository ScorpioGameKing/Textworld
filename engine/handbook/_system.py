from engine.handbook import Command

class System:
    __command_list: dict[str, Command]

    def get_command(self, command_name, *args):
        self.__command_list[command_name]
    
    def add_command(self, command_name, _command:Command):
        self.__command_list[command_name] = _command