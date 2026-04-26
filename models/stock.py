class Stock:
    def __init__(self, id, item_id, location_id, qty):
        self.id = id
        self.item_id = item_id
        self.location_id = location_id
        self.qty = qty

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Stock(**data)