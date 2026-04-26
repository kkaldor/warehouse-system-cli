from repositories.stock_repository import StockRepository
from models.stock import Stock
from core.utils import generate_id

class StockService:
    def __init__(self):
        self.repo = StockRepository()

    def get_stock(self, item_id, location_id):
        stocks = self.repo.load_all()
        for s in stocks:
            if s.item_id == item_id and s.location_id == location_id:
                return s
        return None

    def add_stock(self, item_id, location_id, qty):
        if qty <= 0:
            raise ValueError("Quantity harus lebih besar dari 0")

        existing = self.get_stock(item_id, location_id)
        if existing:
            existing.qty += qty
            self.repo.update(existing)
        else:
            new_stock = Stock(
                id=generate_id("stock"),
                item_id=item_id,
                location_id=location_id,
                qty=qty
            )
            self.repo.insert(new_stock)

    def reduce_stock(self, item_id, location_id, qty):
        if qty <= 0:
            raise ValueError("Quantity harus lebih besar dari 0")

        existing = self.get_stock(item_id, location_id)
        if not existing:
            raise ValueError("Stok tidak ditemukan pada lokasi tersebut")

        if existing.qty < qty:
            raise ValueError("Stok tidak mencukupi (WMS: no negative stock allowed)")

        existing.qty -= qty
        self.repo.update(existing)

    def list_stock(self):
        return self.repo.load_all()