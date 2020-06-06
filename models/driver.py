from .user import User


class Driver(User):
    def __init__(self, id, name, phone_no, location, vehicle_no):
        super().__init__(id, name, phone_no, location)
        self.vehicle_no = vehicle_no
        self.engaged = False

