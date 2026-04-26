class Item:
    def __init__(self, id, name, sku, category, uom, safety_stock):
        self.id = id
        self.name = name
        self.sku = sku
        self.category = category
        self.uom = uom
        self.safety_stock = safety_stock

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Item(**data)