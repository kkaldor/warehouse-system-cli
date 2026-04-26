from core.base_repository import BaseRepository
from models.location import Location

class LocationRepository(BaseRepository):
    def __init__(self):
        super().__init__("data/locations.json", Location)