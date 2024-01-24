from DataAccess.Domains.Material import Material
from DataAccess.Repositories import MaterialFileRepository
from Infrastructure.Validators.Decorators.DataJsonConverter.DataJsonConverter import converting_data_material_to_json
from Infrastructure.Validators.Decorators.ExceptionHandlers.FileExceptionHandlers import try_handle_log_levels


class MaterialFileService:
    def __init__(self, repository: MaterialFileRepository):
        self._repository = repository

    @try_handle_log_levels('Try to add data to file: ')
    @converting_data_material_to_json
    def add(self, data: Material) -> None:
        self._repository.add(data)

    @try_handle_log_levels('Try to get data from file: ')
    def get(self) -> dict:
        return self._repository.get()

    @try_handle_log_levels('Try to get data by id from file: ')
    def get_by_id(self, id: int) -> dict:
        return self._repository.get_by_id(id)

    @converting_data_material_to_json
    @try_handle_log_levels('Try to update data in file: ')
    def update(self, id: int, data: Material) -> None:
        self._repository.update(id, data)

    @try_handle_log_levels('Try to delete data in file: ')
    def delete(self, id: int) -> None:
        self._repository.delete(id)
