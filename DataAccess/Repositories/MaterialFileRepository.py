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
        return next(filter(lambda x: x[id] == id, self.get()["materials"]))

    def update(self, data):
        previous = self.get()
        MaterialFileRepository.__union(previous, data)
        self.add(previous)

    @staticmethod
    def __union(data1, data2):
        for key, value in data1.items():
            for item in value:
                if not MaterialFileRepository.__includes(item, data2[key]):
                    data1[key].append(item)

    @staticmethod
    def __includes(data1, data2):
        for item in data2:
            _, *current_values = item.values()
            _, *data1_values = data1.values()
            if current_values == data1_values:
                return True
        return False
