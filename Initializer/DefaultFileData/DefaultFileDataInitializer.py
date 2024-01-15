import json

from DataAccess.Contexts.FileDataContext import FileDataContext


class DefaultFileDataInitializer:
    def __init__(self, context: FileDataContext):
        self._context = context

    def initializer(self):
        with open(self._context.path, "w", encoding="utf-8") as file:
            json.dump(self.__get_data(), file, indent=3)

    @staticmethod
    def __get_data():
        return {
            "materials": [
                {
                    "id": 1,
                    "name": "Brick",
                    "price": 200
                },
                {
                    "id": 2,
                    "name": "Wood",
                    "price": 150
                },
                {
                    "id": 3,
                    "name": "Steel",
                    "price": 300
                },
                {
                    "id": 4,
                    "name": "Concrete",
                    "price": 250
                },
                {
                    "id": 5,
                    "name": "Glass",
                    "price": 180
                },
                {
                    "id": 6,
                    "name": "Ceramic Tiles",
                    "price": 220
                },

                {
                    "id": 8,
                    "name": "Marble",
                    "price": 350
                },
                {
                    "id": 9,
                    "name": "Plaster",
                    "price": 170
                },
                {
                    "id": 10,
                    "name": "PVC",
                    "price": 120
                }
            ]
        }
