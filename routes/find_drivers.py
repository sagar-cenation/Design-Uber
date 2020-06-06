from flask import jsonify

from main import app
from services.driver_service import DriverService


@app.route("find/location/<customer_location>")
def get_nearest_driver(customer_location: int):
    driver_service = DriverService()
    drivers = driver_service.get_all_drivers_near_location(customer_location)
    return jsonify(drivers, 200)