from spyne import (
    ComplexModel, String, Integer,
)

class Todos(ComplexModel):
    id = Integer
    user_id = Integer
    title = String
    due_on = String
    status = String

    def __init__(self, id, user_id, title, due_on, status):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.due_on = due_on
        self.status = status

    def __init__(self, dict_data):
        self.id = dict_data["id"]
        self.user_id = dict_data["user_id"]
        self.title = dict_data["title"]
        self.due_on = dict_data["due_on"]
        self.status = dict_data["status"]
