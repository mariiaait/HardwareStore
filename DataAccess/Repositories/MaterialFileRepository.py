import json

from Configuration.config import MATERIALS_JSON_KEY, ENCODING_TYPE, INDENT, MATERIAL_ID
from DataAccess.Contexts import FileDataContext


class MaterialFileRepository:
    def __init__(self, context: FileDataContext):
        self._context = context

    def add(self, data: dict) -> bool:
        current_data = self.get()
        if not MaterialFileRepository.is_exist(data, current_data):
            current_data[MATERIALS_JSON_KEY].append(data)
            self.__write(current_data)
            return True
        return False

    def get(self) -> dict:
        with open(self._context.path, "r", encoding=ENCODING_TYPE) as file:
            return json.load(file)

    def get_by_id(self, id: int) -> dict:
        all_data = self.get()
        return MaterialFileRepository.__get_by_id_from(id, all_data)

    def update(self, data: dict) -> bool:
        all_data = self.get()
        updated_data = all_data

        if MaterialFileRepository.is_exist(data, all_data):
            updated_data = {
                MATERIALS_JSON_KEY: list(
                    map(lambda current: data if current[MATERIAL_ID] == data[MATERIAL_ID] else current,
                        all_data[MATERIALS_JSON_KEY]))}
        else:
            updated_data[MATERIALS_JSON_KEY].append(data)

        self.__write(updated_data)
        return True

    def delete(self, id: int) -> bool:
        all_data = self.get()
        data_to_remove = MaterialFileRepository.__get_by_id_from(id, all_data)
        all_data[MATERIALS_JSON_KEY].remove(data_to_remove)
        self.__write(all_data)
        return True

    def __write(self, data: dict) -> bool:
        with open(self._context.path, "w", encoding=ENCODING_TYPE) as file:
            json.dump(data, file, indent=INDENT)

    @staticmethod
    def __get_by_id_from(id: int, data: dict) -> dict:
        for item in data[MATERIALS_JSON_KEY]:
            if item[MATERIAL_ID] == id:
                return item
        raise Exception(f"Item with id '{id}' was not found")

    @staticmethod
    def is_exist(item: dict, data: dict) -> bool:
        return any(map(lambda element: item[MATERIAL_ID] == element[MATERIAL_ID], data[MATERIALS_JSON_KEY]))
