import json


class MaterialFileRepository:
    def __init__(self, context: FileDataContext):
        self._context = context

    def add(self, data):
        with open(self._context.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=3)

    def get(self):
        with open(self._context.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_by_id(self, id):
        with open(self._context.path, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data["materials"]:
                if item["id"] == id:
                    return item