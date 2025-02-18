from generation import TextworldWorld
from database import WorldDatabase, Database, Color as ColorQueries, World as WorldQueries, Tile as TileQueries
from models import Size

with Database() as db:
    db.init_db(ColorQueries.INIT, ColorQueries.INIT, WorldQueries.INIT, TileQueries.INIT, TileQueries.FILL)

world = TextworldWorld(chunk_count=Size(5,5), chunk_size=Size(150,150))
world.generate_map()
with WorldDatabase() as db:
    db.save_world_to_db(world.save_world(), "Test Saves 4")