import logging
from BusinessLogic.Services.MaterialFileService import MaterialFileService
from DataAccess.Domains.Material import Material

from Infrastructure.Validators.Decorators.TypeChecker import TypeChecker
from Presentation.Response.DataResponse import DataResponse


class MaterialController:
    def __init__(self, service: MaterialFileService):
        self._service = service


    def add(self, data: Material) -> bool:
        try:
            TypeChecker.type_check(self.add, data)
            logging.info(f"Add method was given args: {data}")
            return self._service.add(data)
        except TypeError as ex:
            logging.error(f"{ex} Module: {__name__} Args: {ex.args}")
            return DataResponse(False, None, ex)


    def get(self) -> dict:
        try:
            TypeChecker.type_check(self.get)
            logging.info(f"Get method does not accept parameters")
            return self._service.get()
        except TypeError as ex:
            logging.error(f"{ex} Module: {__name__} Args: {ex.args}")
            return DataResponse(False, None, ex)


    def get_by_id(self, id: int) -> dict:
        try:
            TypeChecker.type_check(self.add, id)
            logging.info(f"Get_by_id method was given args: {id}")
            return self._service.get_by_id(id)
        except TypeError as ex:
            logging.error(f"{ex} Module: {__name__} Args: {ex.args}")
            return DataResponse(False, None, ex)


    def update(self, data: Material) -> bool:
        try:
            TypeChecker.type_check(self.add, data)
            logging.info(f"Update method was given args: {data}")
            return self._service.update(data)
        except TypeError as ex:
            logging.error(f"{ex} Module: {__name__} Args: {ex.args}")
            return DataResponse(False, None, ex)


    def delete(self, id: int) -> bool:
        try:
            TypeChecker.type_check(self.add, id)
            logging.info(f"Delete method was given args: {id}")
            return self._service.delete(id)
        except TypeError as ex:
            logging.error(f"{ex} Module: {__name__} Args: {ex.args}")
            return DataResponse(False, None, ex)
