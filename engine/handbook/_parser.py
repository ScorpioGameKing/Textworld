from kivy.app import App
from engine.handbook._commands import SystemCommands
import logging

class HandbookParser:
    def parse_token_list(self, token_list):
        logging.debug(f"|PARSER| Token List: {token_list}")
        for _t in token_list:
            match _t[1]:
                case "SYS":
                    logging.debug(f"|PARSER| TOKEN: {_t, SystemCommands.COMMANDS.get(tuple(_t))}")
                    _func = SystemCommands.COMMANDS.get(tuple(_t))
                    match _t[0]:
                        case "EXIT":
                            _func[0](world=App.get_running_app().game.screens[1].game_manager.active_world, save_name=App.get_running_app().game.screens[1].game_manager.save_name)
                            break
                        case "EXIT_NS":
                            _func[0]()
                            break
                        case "SAVE":
                            _func[0](world=App.get_running_app().game.screens[1].game_manager.active_world, save_name=App.get_running_app().game.screens[1].game_manager.save_name)
                            break
                case _:
                    logging.debug(f"|PARSER| Either this isn't set up or this isn't a command token: {_t}")
                    break