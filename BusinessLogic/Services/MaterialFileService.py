from HardwareStore.DataAccess.Repositories import MaterialFileRepository


class MaterialFileService:
    def __init__(self, repository: MaterialFileRepository):
        self._repository = repository

    def add(self, data):
        self._repository.add(data)

    def get(self, data):
        try:
            return self._repository(data)
        except ValueError as ex:
            print(ex)



    def get_by_id(self, id):
        try:
            return self._repository(id)
        except ValueError as ex:
            print(ex)

    def update(self, data):
        try:
            return self._repository(data)
        except ValueError as ex:
            print(ex)






