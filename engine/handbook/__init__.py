from engine.handbook.command import Command
from engine.handbook._command_list import CommandList
from engine.handbook._lexer import HandbookLexer
from engine.handbook._sys_commands import cmd_data

class HandbookLang():

    _sys_commands:CommandList
    _user_commands:CommandList

    def __init__(self):
        self.lexer = HandbookLexer()
        self._sys_commands = CommandList()
        self._user_commands = CommandList()
        self.build_default_commands()

    def build_default_commands(self):
        print(cmd_data.commands)