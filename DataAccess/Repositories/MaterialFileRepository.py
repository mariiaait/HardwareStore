import json


class MaterialFileRepository:
    def __init__(self, context: FileDataContext):
        self._context = context

    def add(self, data):
        with open(self._context.path, "a", encoding="utf-8") as file:
            json.dump(data, file, indent=3)

    def get(self):
        with open(self._context.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_by_id(self, id):
        return filter(lambda x: x[id] == id, self.get()["materials"])
