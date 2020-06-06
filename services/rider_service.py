import logging

from services.driver_service import DriverService


class RiderService:
    def __init__(self):
        self.driver_service = DriverService()

    def request_ride(self, driver_id, location):
        logging.info("Requesting ride for: %s for location: %s", driver_id, location)
        return self.driver_service.confirm_request(driver_id, location)
