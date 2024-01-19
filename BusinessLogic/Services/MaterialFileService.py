from DataAccess.Repositories import MaterialFileRepository
from Infrastructure.Validators.Decorators import try_handle_log_levels

import datetime

class MaterialFileService:
    def __init__(self, repository: MaterialFileRepository):
        self._repository = repository

    @try_handle_log_levels(log_mes='ERROR:{0}'.format(datetime.datetime.now()))
    def add(self, data):
        self._repository.add(data)

    @try_handle_log_levels(log_mes='ERROR:{0}'.format(datetime.datetime.now()))
    def get(self):
        return self._repository.get()

    @try_handle_log_levels(log_mes='ERROR:{0}'.format(datetime.datetime.now()))
    def get_by_id(self, id):
        return self._repository.get_by_id(id)

    @try_handle_log_levels(log_mes='ERROR:{0}'.format(datetime.datetime.now()))
    def update(self, id, data):
        self._repository.update(id, data)

    @try_handle_log_levels(log_mes='ERROR:{0}'.format(datetime.datetime.now()))
    def delete(self, id):
        self._repository.delete(id)

