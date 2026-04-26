class Location:
    def __init__(self, id, warehouse, rack, aisle, bin_code):
        self.id = id
        self.warehouse = warehouse
        self.rack = rack
        self.aisle = aisle
        self.bin_code = bin_code

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Location(**data)