class Tokens:
    TOKENS:dict[str, str] = { # TOKENS:dict[str, dict[str]] to allow for top level search of command type ie, SYS, ACT, REL
        # System Command Tokens
        "EXIT" : "SYS",
        "EXIT_NS" : "SYS",
        "SAVE" : "SYS",
        "DUMP_MAP": "SYS",
        "SPAWN_MOB": "SYS",

        # Game Command Tokens
        "MOVE" : "ACT",
        "INSPECT" : "ACT",
        "SPEAK" : "ACT",
        "PUSH" : "ACT",
        "ATTACK" : "ACT",
        "CROUCH" : "ACT",
        "LISTEN" : "ACT",

        # Relation Tokens
        "WITH" : "REL",
        "AND" : "REL",
        "TO" : "REL",

        # Direction Tokens
        "NORTH" : "DIR",
        "SOUTH" : "DIR",
        "EAST" : "DIR",
        "WEST" : "DIR"
    }
    