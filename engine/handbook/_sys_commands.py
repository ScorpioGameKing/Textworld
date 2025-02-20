from engine.handbook import Command, CommandList

class SysCommands(CommandList):

    def build_system_commands(self):
        self.command_list["SYS", self._sys_EXIT("Exit", self._sys_EXIT._sys_exit)]
        print(self.commands)

    class _sys_EXIT(Command):
        def _sys_exit():
            print("Exit")