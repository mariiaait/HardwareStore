import json

from HardwareStore.DataAccess.Contexts import FileDataContext


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
        return next(filter(lambda x: x['id'] == id, self.get()["materials"]))

    def update(self, id, data):
        all_data = self.get()
        updated_data = {"materials": list(map(lambda current: data if current['id'] == id else current, all_data["materials"]))}
        self.__write(updated_data)

    def __write(self, data):
        with open(self._context.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=3)

    def delete(self, id):
        data_to_remove = self.get_by_id(id)
        all_data = self.get()
        all_data.remove(data_to_remove)
        self.__write(all_data)
