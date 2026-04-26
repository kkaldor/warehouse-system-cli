import json
import os

class BaseRepository:
    def __init__(self, file_path, model_class):
        self.file_path = file_path
        self.model_class = model_class

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f)

    def load_all(self):
        with open(self.file_path, "r") as f:
            data = json.load(f)
            return [self.model_class.from_dict(d) for d in data]

    def save_all(self, objects):
        with open(self.file_path, "w") as f:
            json.dump([obj.to_dict() for obj in objects], f, indent=2)

    def find_by_id(self, obj_id):
        return next((o for o in self.load_all() if o.id == obj_id), None)

    def insert(self, obj):
        data = self.load_all()
        data.append(obj)
        self.save_all(data)

    def update(self, updated_obj):
        data = self.load_all()
        new_data = []
        for obj in data:
            if obj.id == updated_obj.id:
                new_data.append(updated_obj)
            else:
                new_data.append(obj)
        self.save_all(new_data)