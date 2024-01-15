import json


class MaterialFileRepository:
    def __init__(self, context: FileDataContext):
        self._context = context

    def add(self, data):
            current_data = self.get()
            current_data["materials"].append(data)
            with open(self._context.path, "w", encoding="utf-8") as file:
                json.dump(current_data, file, indent=3)


    def get(self):
        try:
            with open(self._context.path, "r", encoding="utf-8") as file:
            return json.load(file)
        except json.JSONDecodeError:
            json.dump({"materials": []}, file, indent=3)

    def get_by_id(self, id):
        result = next(map(lambda x: x[id], filter(lambda x: x[id] == id, self.get()["materials"])))
        return result
