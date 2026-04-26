from core.base_repository import BaseRepository
from models.item import Item

class ItemRepository(BaseRepository):
    def __init__(self):
        super().__init__("data/items.json", Item)