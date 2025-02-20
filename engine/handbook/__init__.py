from engine.handbook.command import Command
from engine.handbook._command_list import CommandList
from engine.handbook._lexer import HandbookLexer
from engine.handbook._sys_commands import SysCommands

class HandbookLang():

    def __init__(self):
        self.lexer = HandbookLexer()
        self._sys_commands = SysCommands()

    # KEY ERRORs are pain
    def build_default_commands(self):
        self._sys_commands.build_system_commands()