from kivy.app import App
from engine.database import WorldDatabase
from models import Coords
import logging

class SystemCommands:

    def _save_game(world, save_name):
        logging.debug(f"Saving: {save_name}")
        with WorldDatabase() as db:
                db.save_world_to_db(world.save_world(), save_name)

    def _exit_game_no_save():
        logging.debug("Exiting with No Save")
        App.get_running_app().game.current = 'main_menu_ui'

    def _dump_map(gm, pos:tuple[int, int] = None):
        if pos == None:
            logging.debug(f"Dumping: {gm.world_position}")
            gm.active_world.dump_chunk(gm.world_position)
        else:
            logging.debug(f"Dumping: {pos}")
            gm.active_world.dump_chunk(Coords(*pos))
    
    def _exit_game(world, save_name):
        logging.debug(f"Saving and Exiting: {save_name}")
        with WorldDatabase() as db:
                db.save_world_to_db(world.save_world(), save_name)
        App.get_running_app().game.current = 'main_menu_ui'

    COMMANDS:dict[tuple[str,str], tuple[callable, int]] = {
        ("EXIT", "SYS") : [_exit_game, 0],
        ("EXIT_NS", "SYS") : [_exit_game_no_save, 0],
        ("SAVE", "SYS") : [_save_game, 0],
        ("DUMP_MAP", "SYS") : [_dump_map, 2]
    }