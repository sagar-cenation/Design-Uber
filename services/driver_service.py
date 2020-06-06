import logging
from constants import LOCATION_RANGE


class DriverService:
    def __init__(self):
        self.drivers_list = dict()

    def get_all_drivers(self):
        # DB Call
        return self.drivers_list

    def notify_driver(self, driver_id: str, location: int):
        # API Call - true, false, network error
        logging.info("Notifying driver for the ride: %s", driver_id)
        return True # change it when actual api calls

    def get_all_drivers_near_location(self, customer_location: int) -> list:
        """Fetches all drivers near the given location
        """
        logging.info("Fetching all drivers")
        nearby_drivers = []
        all_drivers = self.get_all_drivers()

        for driver in all_drivers.values():
            if abs(driver.location - customer_location) <= LOCATION_RANGE and not driver.engaged:
                nearby_drivers.append(driver)
        logging.info("Found %s drivers near %s location", len(all_drivers), customer_location)
        return nearby_drivers

    def confirm_request(self, driver_id: str, location: int) -> bool:
        try:
            confirmation = self.notify_driver(driver_id, location)
            self.drivers_list[driver_id] = confirmation
            return confirmation
        except Exception as exception:
            logging.exception("Error occurred in confirming the request: %s", exception)
            raise Exception("Temporary Unavailable") # replace with custom exception
