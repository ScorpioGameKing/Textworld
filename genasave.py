from generation import TextworldWorld
from database import WorldDatabase
from models import Size

world = TextworldWorld(chunk_count=Size(10,10), chunk_size=Size(250,250))
with WorldDatabase() as db:
    db.save_world_to_db(world.save_world(), "Test Saves 3")