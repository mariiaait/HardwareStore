class MaterialController:
    def __init__(self, service):
        self._service = service

    def add(self, data):
        self._service.add(data)

    def get(self, service):
        return self._service.get()

    def get_by_id(self, id):
        return self._service.get_by_id(id)

    def update(self, id, data):
        self._service.update(id, data)

    def delete(self, id):
        self._service.delete(id)
