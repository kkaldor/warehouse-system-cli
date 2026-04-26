from core.base_repository import BaseRepository
from models.stock import Stock

class StockRepository(BaseRepository):
    def __init__(self):
        super().__init__("data/stocks.json", Stock)