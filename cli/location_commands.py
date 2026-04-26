from core.location_service import LocationService

class LocationCommands:
    def __init__(self):
        self.service = LocationService()

    def handle(self, sub, args):
        if sub == "create":
            self.create_location()
        elif sub == "list":
            self.list_locations()
        else:
            print("Subcommand location tidak valid")

    def create_location(self):
        warehouse = input("Warehouse: ")
        rack = input("Rack: ")
        aisle = input("Aisle: ")
        bin_code = input("Bin Code: ")

        self.service.create_location(warehouse, rack, aisle, bin_code)
        print("Lokasi berhasil dibuat")

    def list_locations(self):
        locations = self.service.list_locations()
        print("\n=== Daftar Lokasi ===")
        for l in locations:
            print(f"{l.id} | {l.warehouse} | {l.rack}-{l.aisle}-{l.bin_code}")