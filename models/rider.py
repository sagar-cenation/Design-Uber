from .user import User


class Rider(User):
    def __init__(self, id, name, phone_no, location):
        super().__init__(id, name, phone_no, location)

