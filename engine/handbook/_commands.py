from kivy.app import App
from database import WorldDatabase
import logging

class SystemCommands:

    def _save_game(world, save_name):
        logging.debug(f"Saving: {save_name}")
        with WorldDatabase() as db:
                db.save_world_to_db(world.save_world(), save_name)

    def _exit_game_no_save():
        logging.debug("Exiting with No Save")
        App.get_running_app().game.current = 'main_menu_ui'
    
    def _exit_game(world, save_name):
        logging.debug(f"Saving and Exiting: {save_name}")
        with WorldDatabase() as db:
                db.save_world_to_db(world.save_world(), save_name)
        App.get_running_app().game.current = 'main_menu_ui'

    COMMANDS:dict[tuple[str,str], tuple[callable, int]] = {
        ("EXIT", "SYS") : [_exit_game, 2],
        ("EXIT_NS", "SYS") : [_exit_game_no_save, 0],
        ("SAVE", "SYS") : [_save_game, 2]
    }