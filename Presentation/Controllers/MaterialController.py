
class Controller:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def get(self):
        return self.data

    def get_by_id(self, item_id):
        for item in self.data:
            if item.id == item_id:
                return item
        return None

    def update(self, item_id, new_data):
        for i, item in enumerate(self.data):
            if item.id == item_id:
                self.data[i] = new_data
                break

    def delete(self, item_id):
        self.data = [item for item in self.data if item.id != item_id]