from BusinessLogic.Services.MaterialFileService import MaterialFileService
from DataAccess.Domains.Material import Material


class MaterialController:
    def __init__(self, service: MaterialFileService):
        self._service = service

    def add(self, data: Material) -> None:
        self._service.add(data)

    def get(self) -> dict:
        return self._service.get()

    def get_by_id(self, id: int) -> dict:
        return self._service.get_by_id(id)

    def update(self, id: int, data: Material) -> None:
        self._service.update(id, data)

    def delete(self, id: int) -> None:
        self._service.delete(id)
