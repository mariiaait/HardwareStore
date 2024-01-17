from DataAccess.Repositories import MaterialFileRepository


class MaterialFileService:
    def __init__(self, repository: MaterialFileRepository):
        self._repository = repository

    def add(self, data):
        try:
            self._repository.add(data)
        except FileNotFoundError:
            pass

    def get(self):
        try:
            return self._repository.get()
        except FileNotFoundError:
            pass

    def get_by_id(self, id):
        try:
            return self._repository.get_by_id(id)
        except FileNotFoundError:
            pass

    def update(self, id, data):
        try:
            return self._repository.update(id, data)
        except FileNotFoundError:
            pass

    def delete(self, id):
        try:
            return self._repository.delete(id)
        except FileNotFoundError:
            pass







