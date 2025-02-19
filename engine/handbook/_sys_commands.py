from engine.handbook import Command, CommandList

sys_cmds:CommandList

def __init__(self):
    print(self.commands)

def _sys_EXIT(self):
    pass

sys_cmds.append("Exit", Command("Exit",_sys_EXIT))