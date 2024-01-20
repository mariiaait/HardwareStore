import json

from Configuration.config import MATERIALS_JSON_KEY, ENCODING_TYPE, INDENT
from DataAccess.Contexts import FileDataContext


class MaterialFileRepository:
    def __init__(self, context: FileDataContext):
        self._context = context

    def add(self, data):
        current_data = self.get()
        current_data[MATERIALS_JSON_KEY].append(data)
        self.__write(current_data)

    def get(self):
        try:
            with open(self._context.path, "r", encoding=ENCODING_TYPE) as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {MATERIALS_JSON_KEY: []}

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
        with open(self._context.path, "w", encoding=ENCODING_TYPE) as file:
            json.dump(data, file, indent=INDENT)

    @staticmethod
    def __get_by_id_from(id, data):
        for item in data["materials"]:
            if item["id"] == id:
                return item
        raise Exception(f"Item with id '{id}' was not found")
