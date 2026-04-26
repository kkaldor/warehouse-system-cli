from core.stock_service import StockService

class StockCommands:
    def __init__(self):
        self.service = StockService()

    def handle(self, sub, args):
        if sub == "add":
            self.add_stock()
        elif sub == "reduce":
            self.reduce_stock()
        elif sub == "list":
            self.list_stock()
        else:
            print("Subcommand stok tidak valid")

    def add_stock(self):
        item_id = input("Item ID: ")
        location_id = input("Location ID: ")
        qty = int(input("Qty masuk: "))

        try:
            self.service.add_stock(item_id, location_id, qty)
            print("Stok berhasil ditambahkan")
        except Exception as e:
            print("Error:", e)

    def reduce_stock(self):
        item_id = input("Item ID: ")
        location_id = input("Location ID: ")
        qty = int(input("Qty keluar: "))

        try:
            self.service.reduce_stock(item_id, location_id, qty)
            print("Stok berhasil dikurangi")
        except Exception as e:
            print("Error:", e)

    def list_stock(self):
        stocks = self.service.list_stock()
        print("\n=== Daftar Stok ===")
        for s in stocks:
            print(f"{s.item_id} | {s.location_id} | {s.qty}")