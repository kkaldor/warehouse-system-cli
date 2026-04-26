from repositories.item_repository import ItemRepository
from core.utils import generate_id
from models.item import Item
from cli.stock_commands import StockCommands
from cli.location_commands import LocationCommands

class CommandHandler:

    def __init__(self):
        self.item_repo = ItemRepository()

    def handle(self, command, subcommand, args):
        if command == "item":
            self.handle_item(subcommand, args)
        elif command == "stock":
             stock = StockCommands()
             stock.handle(subcommand, args)
        elif command == "location":
             loc = LocationCommands()
             loc.handle(subcommand, args)
        else:
            print("Command tidak dikenali")

    def handle_item(self, subcommand, args):
        if subcommand == "create":
            name = input("Nama: ")
            sku = input("SKU: ")
            category = input("Kategori: ")
            uom = input("UOM: ")
            safety_stock = int(input("Safety Stock: "))

            item = Item(
                id=generate_id("item"),
                name=name,
                sku=sku,
                category=category,
                uom=uom,
                safety_stock=safety_stock
            )

            self.item_repo.insert(item)
            print("Item berhasil dibuat")

        elif subcommand == "list":
            items = self.item_repo.load_all()
            for i in items:
                print(f"{i.id} | {i.name} | {i.sku}")

        else:
            print("Subcommand item tidak valid")