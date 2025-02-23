class Tokens:
    TOKENS:dict[str, str] = {
        # System Command Tokens
        "EXIT" : "SYS",
        "EXIT_NS" : "SYS",
        "SAVE" : "SYS",

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
    