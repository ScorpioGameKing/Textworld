from engine.handbook import Command

class CommandList:
    command_list: dict[str, Command]
    
    def __init__(self):
        self.command_list = dict[str]

    def get_command(self, command_name, *args):
        self.command_list[command_name]

    def add_command(self, command_name, cmd:Command):
        self.command_list[command_name] = cmd