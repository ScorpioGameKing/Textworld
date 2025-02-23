from engine.handbook._commands import SystemCommands
import logging

class HandbookParser:
    def parse_token_list(self, token_list):
        logging.debug(f"|PARSER| Token List: {token_list}")
        for _t in token_list:
            match _t[1]:
                case "SYS":
                    logging.debug(f"|PARSER| TOKEN: {_t, SystemCommands.COMMANDS.get(tuple(_t))}")
                    SystemCommands.COMMANDS.get(tuple(_t))()
                    break
                case _:
                    logging.debug(f"|PARSER| Either this isn't set up or this isn't a command token: {_t}")