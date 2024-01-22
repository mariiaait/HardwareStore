import json

from Configuration.config import MATERIALS_JSON_KEY, ENCODING_TYPE, INDENT, MATERIAL_ID
from DataAccess.Contexts import FileDataContext


class MaterialFileRepository:
    def __init__(self, context: FileDataContext):
        self._context = context

    def add(self, data: dict) -> None:
        current_data = self.get()
        current_data[MATERIALS_JSON_KEY].append(data)
        self.__write(current_data)

    def get(self) -> dict:
        with open(self._context.path, "r", encoding=ENCODING_TYPE) as file:
            return json.load(file)

    def get_by_id(self, id: int) -> dict:
        all_data = self.get()
        return MaterialFileRepository.__get_by_id_from(id, all_data)

    def update(self, id: int, data: int) -> None:
        all_data = self.get()
        updated_data = {
            MATERIALS_JSON_KEY: list(
                map(lambda current: data if current[MATERIAL_ID] == id else current, all_data[MATERIALS_JSON_KEY]))}
        if all_data == updated_data:
            updated_data[MATERIALS_JSON_KEY].append(data)

        self.__write(updated_data)

    def delete(self, id: int) -> None:
        all_data = self.get()
        data_to_remove = MaterialFileRepository.__get_by_id_from(id, all_data)
        all_data[MATERIALS_JSON_KEY].remove(data_to_remove)
        self.__write(all_data)

    def __write(self, data: dict) -> None:
        with open(self._context.path, "w", encoding=ENCODING_TYPE) as file:
            json.dump(data, file, indent=INDENT)

    @staticmethod
    def __get_by_id_from(id: int, data: dict) -> dict:
        for item in data[MATERIALS_JSON_KEY]:
            if item[MATERIAL_ID] == id:
                return item
        raise Exception(f"Item with id '{id}' was not found")
