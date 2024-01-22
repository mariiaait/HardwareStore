import json

from Configuration.config import MATERIALS_JSON_KEY, ENCODING_TYPE, INDENT, MATERIAL_ID
from DataAccess.Contexts import FileDataContext


class MaterialFileRepository:
    """Class for adding, getting, updating and deleting of data in repository. Writing to file"""

    def __init__(self, context: FileDataContext):
        self._context = context

    def add(self, data):
        """Add data to repository"""
        current_data = self.get()
        current_data[MATERIALS_JSON_KEY].append(data)
        self.__write(current_data)

    def get(self):
        """Get data from repository"""
        try:
            with open(self._context.path, "r", encoding=ENCODING_TYPE) as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {MATERIALS_JSON_KEY: []}

    def get_by_id(self, id):
        """Get data from repository by id"""
        all_data = self.get()
        MaterialFileRepository.__get_by_id_from(id, all_data)

    def update(self, id, data):
        """Update data in repository by id"""
        all_data = self.get()
        updated_data = {
            MATERIALS_JSON_KEY: list(map(lambda current: data if current[MATERIAL_ID] == id else current, all_data[MATERIALS_JSON_KEY]))}
        self.__write(updated_data)

    def delete(self, id):
        """Delete data in repository by id"""
        all_data = self.get()
        data_to_remove = MaterialFileRepository.__get_by_id_from(id, all_data)
        all_data.remove(data_to_remove)
        self.__write(all_data)

    def __write(self, data):
        """Write data to the file"""
        with open(self._context.path, "w", encoding=ENCODING_TYPE) as file:
            json.dump(data, file, indent=INDENT)

    @staticmethod
    def __get_by_id_from(id, data):
        """Returning item by id from data"""
        for item in data[MATERIALS_JSON_KEY]:
            if item[MATERIAL_ID] == id:
                return item
        raise Exception(f"Item with id '{id}' was not found")
