from engine.handbook import Command

class CommandList:
    command_list: dict[str, Command] = {}

    def __getstate__(self):
        return(self.command_list)

    def __getstate__(self, state):
        self.command_list = state