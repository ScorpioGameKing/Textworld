from kivy.app import App
from engine.database import WorldDatabase, EntityDatabase
from models import Coords
import logger
class SystemCommands:

    def _save_game(world, save_name):
        logger.debug(f"Saving: {save_name}")
        with WorldDatabase() as db:
                db.save_world_to_db(world.save_world(), save_name)

    def _exit_game_no_save():
        logger.debug("Exiting with No Save")
        App.get_running_app().game.current = 'main_menu_ui'

    def _dump_map(gm, pos:tuple[int, int] = None):
        if pos == None:
            logger.debug(f"Dumping: {gm.world_position}")
            gm.active_world.dump_chunk(gm.world_position)
        else:
            logger.debug(f"Dumping: {pos}")
            gm.active_world.dump_chunk(Coords(*pos))
    
    def _exit_game(world, save_name):
        logger.debug(f"Saving and Exiting: {save_name}")
        with WorldDatabase() as db:
                db.save_world_to_db(world.save_world(), save_name)
        App.get_running_app().game.current = 'main_menu_ui'

    def _spawn_mob(gm, pos:tuple[int, int], name: str):
        with EntityDatabase() as edb:
            mob = edb.select_mob_by_name(name)
            mob.tile.position = Coords(*pos)
            gm.active_map.set_entity_coords(mob.tile.position, mob)

    COMMANDS:dict[tuple[str,str], tuple[callable, int]] = {
        ("EXIT", "SYS") : [_exit_game, 0],
        ("EXIT_NS", "SYS") : [_exit_game_no_save, 0],
        ("SAVE", "SYS") : [_save_game, 0],
        ("DUMP_MAP", "SYS") : [_dump_map, 2],
        ("SPAWN_MOB", "SYS") : [_spawn_mob, 3]
    }