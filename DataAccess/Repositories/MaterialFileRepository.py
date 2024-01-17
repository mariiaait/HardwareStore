import json

from DataAccess.Contexts import FileDataContext


class MaterialFileRepository:
    def __init__(self, context: FileDataContext):
        self._context = context

    def add(self, data):
        current_data = self.get()
        current_data["materials"].append(data)
        self.__write(current_data)

    def get(self):
        try:
            with open(self._context.path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {"materials": []}

    def get_by_id(self, id):
        all_data = self.get()
        MaterialFileRepository.__get_by_id_from(id, all_data)

    def update(self, id, data):
        all_data = self.get()
        updated_data = {
            "materials": list(map(lambda current: data if current['id'] == id else current, all_data["materials"]))}
        self.__write(updated_data)

    def delete(self, id):
        all_data = self.get()
        data_to_remove = MaterialFileRepository.__get_by_id_from(id, all_data)
        all_data.remove(data_to_remove)
        self.__write(all_data)

    def __write(self, data):
        with open(self._context.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=3)

    @staticmethod
    def __get_by_id_from(id, data):
        for item in data["materials"]:
            if item["id"] == id:
                return item
        raise Exception(f"Item with id '{id}' was not found")
