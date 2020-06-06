from flask import jsonify

from main import app
from services.rider_service import RiderService


@app.route("request/driver/<driver_id>/location/<customer_location>")
def request_ride(driver_id: str, customer_location: int):
    rider_service = RiderService()
    drivers = rider_service.request_ride(driver_id, customer_location)
    return jsonify(drivers, 200)