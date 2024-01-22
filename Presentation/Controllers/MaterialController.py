from BusinessLogic.Services.MaterialFileService import MaterialFileService
from DataAccess.Domains.Material import Material

from HardwareStore.Infrastructure.Validators.Decorators.TypeChecker import type_check_decorator


class MaterialController:
    def __init__(self, service: MaterialFileService):
        self._service = service

    @type_check_decorator
    def add(self, data: Material) -> None:
        self._service.add(data)

    @type_check_decorator
    def get(self) -> dict:
        return self._service.get()

    @type_check_decorator
    def get_by_id(self, id: int) -> dict:
        return self._service.get_by_id(id)

    @type_check_decorator
    def update(self, id: int, data: Material) -> None:
        self._service.update(id, data)

    @type_check_decorator
    def delete(self, id: int) -> None:
        self._service.delete(id)
