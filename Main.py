import json
class Repository:
    def __init__(self, context):
        self._context = context
    def update(self, context_id, new_data):
        if context_id in self._context:
            self._context[context_id].update(new_data)
            print(f"Data for element {context_id} was update.")
        else:
            print(f"{context_id} has not found")
    def add(self, context_id, context_data):
        if context_id not in self._context:
            self._context[context_id] = context_data
            print(f"A new element add to repository {context_id}")
        else:
            print(f"Element {context_id} is already in repository")
    def get(self):
        with open(self._context.path, "r") as file:
            return json.load(file)