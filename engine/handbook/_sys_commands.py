from engine.handbook.command import Command

class cmd_data:
    commands:list
    def __init__(self):
        self.commands.append(["SYS", Command("Exit",self._sys_EXIT)])
        print(self.commands)

    def _sys_EXIT(self):
        pass