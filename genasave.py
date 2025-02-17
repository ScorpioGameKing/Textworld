from generation import TextworldWorld
from database import WorldDatabase
from models import Size

world = TextworldWorld(chunk_count=Size(5,5), chunk_size=Size(150,150))
world.generate_map()
with WorldDatabase() as db:
    db.save_world_to_db(world.save_world(), "Test Saves 4")